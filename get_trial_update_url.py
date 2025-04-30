import os
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from random import choice, randint
from time import time
from urllib.parse import urlsplit, urlunsplit
import requests
from requests.exceptions import Timeout, ConnectionError
from threading import Lock

# Assuming these modules and functions are defined elsewhere
from apis import PanelSession, TempEmail, guess_panel, panel_class_map
from subconverter import gen_base64_and_clash_config, get
from utils import (clear_files, g0, keep, list_file_paths, list_folder_paths,
                  rand_id, read, read_cfg, remove, size2str, str2timestamp,
                  timestamp2str, to_zero, write, write_cfg)

# Thread-safe lock for shared resources
cache_lock = Lock()

def get_sub(session: PanelSession, opt: dict, cache: dict[str, list[str]], log: list):
    """Fetch subscription information with timeout and detailed exception handling."""
    url = cache['sub_url'][0]
    suffix = ' - ' + g0(cache, 'name')
    if 'speed_limit' in opt:
        suffix += ' ⚠️限速 ' + opt['speed_limit']
    
    log.append(f"Starting subscription fetch: {url}")
    try:
        # Adding a 10-second timeout to prevent hanging
        response = requests.get(url, timeout=10)
        info = response.json()  # Assuming JSON response
        log.append(f"Successfully fetched subscription: {url}")
        return [info]  # Compatible with try_turn return format
    except Timeout:
        log.append(f"Subscription fetch timed out: {url}")
        raise
    except ConnectionError:
        log.append(f"Connection error during fetch: {url}")
        raise
    except Exception as e:
        log.append(f"Failed to fetch subscription: {url}, Error: {e}")
        with cache_lock:
            origin = urlsplit(session.origin)[:2]
            url = '|'.join(urlunsplit(origin + urlsplit(part)[2:]) for part in url.split('|'))
        raise

def try_turn(session: PanelSession, opt: dict, cache: dict[str, list[str]], log: list):
    """Attempt to update subscription with improved error handling and logging."""
    with cache_lock:
        cache.pop('更新旧订阅失败', None)
        cache.pop('更新订阅链接/续费续签失败', None)
        cache.pop('获取订阅失败', None)

    log.append(f"Attempting to update subscription: {session.host}")
    try:
        # Assuming should_turn is defined and returns turn and sub
        turn, *sub = should_turn(session, opt, cache)
    except Exception as e:
        with cache_lock:
            cache['更新旧订阅失败'] = [str(e)]
        log.append(f'Failed to update old subscription ({session.host})({cache["sub_url"][0]}): {e}')
        return None

    if turn:
        try:
            # Assuming do_turn is defined
            do_turn(session, opt, cache, log, force_reg=turn == 2)
            log.append(f"Subscription update executed successfully: {session.host}")
        except Exception as e:
            with cache_lock:
                cache['更新订阅链接/续费续签失败'] = [str(e)]
            log.append(f'Failed to update/renew subscription ({session.host}): {e}')
            return sub
        try:
            sub = get_sub(session, opt, cache, log)
            log.append(f"Successfully fetched new subscription: {session.host}")
        except Exception as e:
            with cache_lock:
                cache['获取订阅失败'] = [str(e)]
            log.append(f'Failed to fetch subscription ({session.host})({cache["sub_url"][0]}): {e}')

    return sub

def cache_sub_info(info, opt: dict, cache: dict[str, list[str]], log: list):
    """Cache subscription info with key/value validation."""
    if not info:
        log.append("Subscription info is empty")
        raise Exception('no sub info')
    
    log.append("Starting to cache subscription info")
    try:
        used = float(info["upload"]) + float(info["download"])
        total = float(info["total"])
        rest = '(剩余 ' + size2str(total - used)
        if opt.get('expire') == 'never' or not info.get('expire'):
            expire = '永不过期'
        else:
            ts = str2timestamp(info['expire'])
            expire = timestamp2str(ts)
            rest += ' ' + str(timedelta(seconds=ts - time()))
        rest += ')'
        with cache_lock:
            cache['sub_info'] = [size2str(used), size2str(total), expire, rest]
        log.append("Successfully cached subscription info")
    except KeyError as e:
        log.append(f"Missing key in subscription info: {e}")
        raise
    except ValueError as e:
        log.append(f"Invalid value in subscription info: {e}")
        raise

def save_sub_base64_and_clash(base64, clash, host, opt: dict):
    """Save base64 and Clash configuration."""
    log.append(f"Starting to save subscription config: {host}")
    try:
        result = gen_base64_and_clash_config(
            base64_path=f'trials/{host}',
            clash_path=f'trials/{host}.yaml',
            providers_dir=f'trials_providers/{host}',
            base64=base64,
            clash=clash,
            exclude=opt.get('exclude')
        )
        log.append(f"Successfully saved subscription config: {host}")
        return result
    except Exception as e:
        log.append(f"Failed to save subscription config: {host}, Error: {e}")
        raise

def save_sub(info, base64, clash, base64_url, clash_url, host, opt: dict, cache: dict[str, list[str]], log: list):
    """Save subscription data with optimized error handling."""
    with cache_lock:
        cache.pop('保存订阅信息失败', None)
        cache.pop('保存base64/clash订阅失败', None)

    try:
        cache_sub_info(info, opt, cache, log)
    except Exception as e:
        with cache_lock:
            cache['保存订阅信息失败'] = [str(e)]
        log.append(f'Failed to save subscription info ({host})({clash_url}): {e}')

    try:
        node_n = save_sub_base64_and_clash(base64, clash, host, opt)
        with cache_lock:
            if (d := node_n - int(g0(cache, 'node_n', 0))) != 0:
                log.append(f'{host} node count {"+" if d > 0 else ""}{d} ({node_n})')
            cache['node_n'] = str(node_n)
    except Exception as e:
        with cache_lock:
            cache['保存base64/clash订阅失败'] = [str(e)]
        log.append(f'Failed to save base64/clash subscription ({host})({base64_url})({clash_url}): {e}')

def get_and_save(session: PanelSession, host, opt: dict, cache: dict[str, list[str]], log: list):
    """Fetch and save subscription with thread pool optimization."""
    log.append(f"Starting subscription processing: {host}")
    try_checkin(session, opt, cache, log)  # Assuming this is defined
    sub = try_turn(session, opt, cache, log)
    if sub:
        save_sub(*sub, host, opt, cache, log)
    log.append(f"Completed subscription processing: {host}")

def new_panel_session(host, cache: dict[str, list[str]], log: list) -> PanelSession | None:
    """Create a new session with improved error logging."""
    with cache_lock:
        if 'type' not in cache:
            info = guess_panel(host)
            if 'type' not in info:
                if (e := info.get('error')):
                    log.append(f"{host} type detection failed: {e}")
                else:
                    log.append(f"{host} unknown type")
                return None
            cache.update(info)
    return panel_class_map[g0(cache, 'type')](g0(cache, 'api_host', host), **keep(cache, 'auth_path', getitem=g0))

# Main program with thread pool limiting concurrency
if __name__ == "__main__":
    cache = {'sub_url': ['https://example.com/sub']}
    log = []
    opt = {}
    host = "example.com"
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        session = new_panel_session(host, cache, log)
        if session:
            executor.submit(get_and_save, session, host, opt, cache, log)
    
    # Output logs for debugging
    for entry in log:
        print(entry)
