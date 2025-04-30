import os
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from random import choice, randint
from time import time
from urllib.parse import urlsplit, urlunsplit
import requests
from requests.exceptions import Timeout, ConnectionError
from threading import Lock

# 假设这些模块和函数已定义
from apis import PanelSession, TempEmail, guess_panel, panel_class_map
from subconverter import gen_base64_and_clash_config, get
from utils import (clear_files, g0, keep, list_file_paths, list_folder_paths,
                  rand_id, read, read_cfg, remove, size2str, str2timestamp,
                  timestamp2str, to_zero, write, write_cfg)

# 用于线程安全的锁
cache_lock = Lock()

def get_sub(session: PanelSession, opt: dict, cache: dict[str, list[str]], log: list):
    """获取订阅信息，添加超时和详细异常处理"""
    url = cache['sub_url'][0]
    suffix = ' - ' + g0(cache, 'name')
    if 'speed_limit' in opt:
        suffix += ' ⚠️限速 ' + opt['speed_limit']
    
    log.append(f"开始获取订阅: {url}")
    try:
        # 假设 get 函数使用 requests，添加10秒超时
        response = requests.get(url, timeout=10)
        info = response.json()  # 假设返回 JSON 数据
        log.append(f"成功获取订阅: {url}")
        return [info]  # 返回与 try_turn 兼容的格式
    except Timeout:
        log.append(f"获取订阅超时: {url}")
        raise
    except ConnectionError:
        log.append(f"连接错误: {url}")
        raise
    except Exception as e:
        log.append(f"获取订阅失败: {url}, 错误: {e}")
        with cache_lock:
            origin = urlsplit(session.origin)[:2]
            url = '|'.join(urlunsplit(origin + urlsplit(part)[2:]) for part in url.split('|'))
        raise

def try_turn(session: PanelSession, opt: dict, cache: dict[str, list[str]], log: list):
    """尝试更新订阅，优化错误处理和日志"""
    with cache_lock:
        cache.pop('更新旧订阅失败', None)
        cache.pop('更新订阅链接/续费续签失败', None)
        cache.pop('获取订阅失败', None)

    log.append(f"尝试更新订阅: {session.host}")
    try:
        # 假设 should_turn 已定义，返回 turn 和 sub
        turn, *sub = should_turn(session, opt, cache)
    except Exception as e:
        with cache_lock:
            cache['更新旧订阅失败'] = [str(e)]
        log.append(f'更新旧订阅失败({session.host})({cache["sub_url"][0]}): {e}')
        return None

    if turn:
        try:
            # 假设 do_turn 已定义
            do_turn(session, opt, cache, log, force_reg=turn == 2)
            log.append(f"执行订阅更新成功: {session.host}")
        except Exception as e:
            with cache_lock:
                cache['更新订阅链接/续费续签失败'] = [str(e)]
            log.append(f'更新订阅链接/续费续签失败({session.host}): {e}')
            return sub
        try:
            sub = get_sub(session, opt, cache, log)
            log.append(f"获取新订阅成功: {session.host}")
        except Exception as e:
            with cache_lock:
                cache['获取订阅失败'] = [str(e)]
            log.append(f'获取订阅失败({session.host})({cache["sub_url"][0]}): {e}')

    return sub

def cache_sub_info(info, opt: dict, cache: dict[str, list[str]], log: list):
    """缓存订阅信息，添加键值检查"""
    if not info:
        log.append("订阅信息为空")
        raise Exception('no sub info')
    
    log.append("开始缓存订阅信息")
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
        log.append("缓存订阅信息成功")
    except KeyError as e:
        log.append(f"订阅信息缺少键: {e}")
        raise
    except ValueError as e:
        log.append(f"订阅信息值无效: {e}")
        raise

def save_sub_base64_and_clash(base64, clash, host, opt: dict):
    """保存 base64 和 Clash 配置"""
    log.append(f"开始保存订阅配置: {host}")
    try:
        result = gen_base64_and_clash_config(
            base64_path=f'trials/{host}',
            clash_path=f'trials/{host}.yaml',
            providers_dir=f'trials_providers/{host}',
            base64=base64,
            clash=clash,
            exclude=opt.get('exclude')
        )
        log.append(f"保存订阅配置成功: {host}")
        return result
    except Exception as e:
        log.append(f"保存订阅配置失败: {host}, 错误: {e}")
        raise

def save_sub(info, base64, clash, base64_url, clash_url, host, opt: dict, cache: dict[str, list[str]], log: list):
    """保存订阅数据，优化错误处理"""
    with cache_lock:
        cache.pop('保存订阅信息失败', None)
        cache.pop('保存base64/clash订阅失败', None)

    try:
        cache_sub_info(info, opt, cache, log)
    except Exception as e:
        with cache_lock:
            cache['保存订阅信息失败'] = [str(e)]
        log.append(f'保存订阅信息失败({host})({clash_url}): {e}')

    try:
        node_n = save_sub_base64_and_clash(base64, clash, host, opt)
        with cache_lock:
            if (d := node_n - int(g0(cache, 'node_n', 0))) != 0:
                log.append(f'{host} 节点数 {"+" if d > 0 else ""}{d} ({node_n})')
            cache['node_n'] = str(node_n)
    except Exception as e:
        with cache_lock:
            cache['保存base64/clash订阅失败'] = [str(e)]
        log.append(f'保存base64/clash订阅失败({host})({base64_url})({clash_url}): {e}')

def get_and_save(session: PanelSession, host, opt: dict, cache: dict[str, list[str]], log: list):
    """获取并保存订阅，使用线程池优化并发"""
    log.append(f"开始处理订阅: {host}")
    try_checkin(session, opt, cache, log)  # 假设已定义
    sub = try_turn(session, opt, cache, log)
    if sub:
        save_sub(*sub, host, opt, cache, log)
    log.append(f"完成处理订阅: {host}")

def new_panel_session(host, cache: dict[str, list[str]], log: list) -> PanelSession | None:
    """创建新会话，优化错误日志"""
    with cache_lock:
        if 'type' not in cache:
            info = guess_panel(host)
            if 'type' not in info:
                if (e := info.get('error')):
                    log.append(f"{host} 判别类型失败: {e}")
                else:
                    log.append(f"{host} 未知类型")
                return None
            cache.update(info)
    return panel_class_map[g0(cache, 'type')](g0(cache, 'api_host', host), **keep(cache, 'auth_path', getitem=g0))

# 主程序示例，使用线程池限制并发
if __name__ == "__main__":
    cache = {'sub_url': ['https://example.com/sub']}
    log = []
    opt = {}
    host = "example.com"
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        session = new_panel_session(host, cache, log)
        if session:
            executor.submit(get_and_save, session, host, opt, cache, log)
    
    # 输出日志以便调试
    for entry in log:
        print(entry)
