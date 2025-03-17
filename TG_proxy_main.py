# w1770946466 北慕白  https://github.com/w1770946466/Auto_proxy
# v2ray_collecto
# coding=utf-8
import base64
import requests
import re
import time
import os
import threading
from tqdm import tqdm
import random, string
import datetime
from time import sleep
import chardet

#试用机场链接
home_urls =(

'https://feitucloud.com',
'https://fengqunvpnvip.jmvks.cn',
'https://ff3a7d92-7568-4cca-a053-37087bee70b7.xn--mes358a.art',
'https://fgsfgs.12306.sbs',
'https://fhfdf.ghkjfgjkdfghrjfghjvbnm.cfd',
'https://flare089.sunyi.io',
'https://fly.puroc.cc',
'https://fly0001.buzz',
'https://flybit.pages.dev',
'https://flycnb.tk',
'https://flynb.site',
'https://fn1.170809.xyz',
'https://followcloud.space',
'https://forks.giegie.loan',
'https://free.andiliba.cc',
'https://free.cfnode.shop',
'https://free.colacloud.free.hr',
'https://free.kcjs.me',
'https://free.ninecloud.co',
'https://free.suwas.xyz',
'https://free.vpn66.eu.org',
'https://freeflyingcloud.com',
'https://fs.v2rayse.com',
'https://fs123121.cdn.22.jiacdnd123456789.com',
'https://fsc.jiediandingyuejiji.homes',
'https://fuqing.ch',
'https://fy6.2344599.xyz',
'https://fzdwz.top',
'https://g1.subjsm.cyou',
'https://gates.djjc.cfd',
'https://gateway.51tu.lol',
'https://gauss.life',
'https://gawrgura.moe',
'https://gbshct.spphhnhg.top',
'https://gbtgurl.me',
'https://get.biu001.xyz',
'https://get.ninesub.us.kg',
'https://getinfo.bigbigwatermelon.com',
'https://getinfo.bigwatermelon.org',
'https://gg2.hneko.buzz',
'https://ggiuwegivhe123.a123.bond',
'https://gist.githubusercontent.com',
'https://github.com',
'https://global.tagonline.asia',
'https://go.hhyun.in',
'https://go.yspeed.top',
'https://goodme.pro',
'https://gousstar.cloud',
'https://grslfa.clashx.app',
'https://gs.kkhhddnn.cn',
'https://gsjc.sbs',
'https://guanwang.me',
'https://guolicheng.cfd',
'https://gx.591haoka.com',
'https://gyyun.top',
'https://h.bbydy.org',
'https://hailitum.giountal.top',
'https://haitunyun.online',
'https://haohaoxuexi.qiao1.xyz',
'https://hela.ink',
'https://helloworld-gkhnaabtdcefa9d5.z01.azurefd.net',
'https://hh.haibucuo.xyz',
'https://hh.hnekoo.top',
'https://hneko.top',
'https://hongxingdl.club',
'https://hongxingdl.com',
'https://hongxingdl.love',
'https://host.api-baobaog.rest',
'https://host.ssrbox.com',
'https://hsaii.mejd.cn',
'https://htcmi-20240805.mozhiti.top',
'https://huahe.link',
'https://huaikhwang.central-world.org',
'https://huaxia.tcekx.cn',
'https://huaxia.wueh.cn',
'https://huaxiajichang.cc',
'https://hutaod.com',
'https://hx0618.xn--wqr30o34q.xn--io0a7i',
'https://hx1.starcloud.monster',
'https://hy-2.sbs',
'https://ierboryt.spphhnhg.top',
'https://ifaner.dd94wan.com',
'https://igdux.top',
'https://ihjlkbcueiwqnwior.duboji.vip',
'https://ikuajingbus.com',
'https://ikuntool.com',
'https://inangua.lwjyj.com',
'https://info.iic08924f5w3b65o.xyz',
'https://ins77.link',
'https://install.cdn-sd.xyz',
'https://is7si.cfd',
'https://itdog.cloud',
'https://itjustasub.net',
'https://itjustasub.shop',
'https://j2s.buzz',
'https://jaybest.one',
'https://jb.taipeicity.news',
'https://jc.bbx9527.xyz',
'https://jc.sux.lol',
'https://jc.wingsjiasu.link',
'https://jilu.uuvpn.xyz',
'https://jindoucloud.xyz',
'https://jindouyun88.life',
'https://jiumaojiu.jiumaojiu.net',
'https://jixingnetwork.sbs',
'https://jj.mikasajzy.dynv6.net',
'https://jlhcloud.us.kg',
'https://jmssub.net',
'https://jscr.b-cdn.net',
'https://jshou.top',
'https://jsjc.cfd',
'https://juanwang.site',
'https://juechenyun.top',
'https://juechenyun.xyz',
'https://jxpodzmq93s8etq0.wmcssw.org',
'https://k61kz.no-mad-world.club',
'https://kako.xn--fiq626gzzgkv2a.com',
'https://kalaame.b-cdn.net',
'https://kcssr.ink',
'https://ki.hello1.xyz',
'https://kiking1223.xn--49st2e1z0f.xn--55qx5d',
'https://kiking1223.xn--l6q948csgdz41ai1y.com',
'https://kitsch.xn--8stx8olrwkucjq3b.com',
'https://kkjiasu.top',
'https://kl05.ximicloud.net',
'https://knjc.cfd',
'https://knmvc.site',
'https://kobcloud.com',
'https://kobee.metatai.xyz',
'https://kob-xxkl.top',
'https://koumakan.quickline.top',
'https://ktmcloud.cloud',
'https://ktmcloud.club',
'https://ktmcloud.cool',
'https://ktmcloud.life',
'https://ktmcloud.link',
'https://ktmcloud.lol',
'https://ktmcloud.me',
'https://ktmcloud.men',
'https://ktmcloud.one',
'https://ktmcloud1.club',
'https://ktmurl.club',
'https://ktmurl.top',
'https://kuidingyue.xyz',
'https://kuromisubs.shop',
'https://l.dabai.in',
'https://l.db-link01.top',
'https://lai.sudiudiu.xyz',
'https://landiancc.me',
'https://leseyun.com',
'https://let.bnsubservdom.com',
'https://liangyuandian.club',
'https://liangyuandian.net',
'https://liangyuandian.xyz',
'https://liangyuandian1.com',
'https://lianjia.me',
'https://lianjiajichang.com',
'https://lianjiasub.work',
'https://lianjievpn.com',
'https://liljohnidc.store',
'https://limaiai.net',
'https://link.esnclink.com',
'https://link.kyjc.xyz',
'https://link.rstar.cloud',
'https://link01.fliggylink.xyz',
'https://link02.pikachucloud.site',
'https://link1.db01.in',
'https://link1.db-sub.xyz',
'https://link2.cccc.gg',
'https://link2.proxylink.xyz',
'https://link4.proxylink.xyz',
'https://link5.proxylink.xyz',
'https://linkcube.xyz',
'https://linke.phantasy.life',
'https://liulangdiqiu.cc',
'https://lizhiabc.xyz',
'https://llcool.net',
'https://llgjc.shop',
'https://lmaff01.lmspeed.co',
'https://login.681688.xyz',
'https://login.91unicorn.cc',
'https://login.djjc.cfd',
'https://login.yfjc.xyz',
'https://lonan.sirenyun.me',
'https://lovetalk.tech',
'https://luonan.tech',
'https://ly.ccwink.cc',
'https://lzyjc.xyz',
'https://lzysub.online',
'https://m.o29o.xyz',
'https://m11.spwvpn.com',
'https://m2net.lol',
'https://m2net.sbs',
'https://m33.spwvpn.com',
'https://mac2winer.cfd',
'https://magicae.pics',
'https://maple.icu',
'https://md.tagsub.cf',
'https://mdzz.nmsl.cnmd.ttiktokvpn.top',
'https://meiyiss1.yccch03.top',
'https://meoovpn.net',
'https://meowport.link',
'https://mercedes1208.xn--3iq226gfdb94q.com',
'https://miserableskeletalcpu--jiushinali4.repl.co',
'https://mitce.com',
'https://mlshu.com',
'https://mlshu.xyz',

)
#文件路径
update_path = "./sub/"
#所有的clash订阅链接
end_list_clash = []
#所有的v2ray订阅链接
end_list_v2ray = []
#所有的节点明文信息
end_bas64 = []
#获得格式化后的链接
new_list = []
#永久订阅
e_sub = ['']
#频道
urls =[]
#线程池
threads = []
#机场链接
plane_sub = ['']
#机场试用链接
try_sub = []
#获取频道订阅的个数
sub_n = -25
#试用节点明文
end_try = []

#获取群组聊天中的HTTP链接
def get_channel_http(url):
    headers = {
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://t.me/s/oneclickvpnkeys',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.post(
        url, headers=headers)
    #print(response.text)
    pattren = re.compile(r'"https+:[^\s]*"')
    url_lst = pattren.findall(response.text)
    #print('获取到',len(url_lst),'个网址')
    #print(url_lst)
    return url_lst


#对bs64解密
def jiemi_base64(data):  # 解密base64
    # 对 Base64 编码后的字符串进行解码，得到字节字符串
    decoded_bytes = base64.b64decode(data)
    # 使用 chardet 库自动检测字节字符串的编码格式
    encoding = chardet.detect(decoded_bytes)['encoding']
    # 将字节字符串转换为字符串
    decoded_str = decoded_bytes.decode(encoding)
    return decoded_str

#判读是否为订阅链接
def get_content(url):
    #print('【获取频道',url,'】')
    url_lst = get_channel_http(url)
    #print(url_lst)
    #对链接进行格式化
    for i in url_lst:
        result = i.replace("\\", "").replace('"', "")
        if result not in new_list:
            if "t" not in result[8]:
                if "p" not in result[-2]:
                    new_list.append(result)
    #print(new_list)
    #print("共获得", len(new_list), "条链接")
    #获取单个订阅链接进行判断
    i = 1
    try:
        new_list_down = new_list[sub_n::]
    except:
        new_list_down = new_list[len(new_list) * 2 // 3::]
    #print("共获得", len(new_list_down), "条链接")
    #print('【判断链接是否为订阅链接】')
    for o in new_list_down:
        try:
            res = requests.get(o)
            #判断是否为clash
            try:
                skuid = re.findall('proxies:', res.text)[0]
                if skuid == "proxies:":
                    #print(i, ".这是个clash订阅", o)
                    end_list_clash.append(o)
            except:
                #判断是否为v2
                try:
                    #解密base64
                    peoxy = jiemi_base64(res.text)
                    #print(i, ".这是个v2ray订阅", o)
                    end_list_v2ray.append(o)
                    end_bas64.extend(peoxy.splitlines())
                    
                #均不是则非订阅链接
                except:
                    #print(i, ".非订阅链接")
                    pass
        except:
            #print("第", i, "个链接获取失败跳过！")
            pass
        i += 1
    return end_bas64

#写入文件
def write_document():
    if e_sub == [] or try_sub == []:
        print("订阅为空请检查！")
    else:
        #永久订阅
        random.shuffle(e_sub)
        for e in e_sub:
            try:
                res = requests.get(e)
                proxys=jiemi_base64(res.text)
                end_bas64.extend(proxys.splitlines())
            except:
                print(e,"永久订阅出现错误❌跳过")
        print('永久订阅更新完毕')
        #试用订阅
        random.shuffle(try_sub)
        for t in try_sub:
            try:
                res = requests.get(t)
                proxys=jiemi_base64(res.text)
                end_try.extend(proxys.splitlines())
            except Exception as er:
                print(t,"试用订阅出现错误❌跳过",er)
        print('试用订阅更新完毕',try_sub)
        #永久订阅去重
        end_bas64_A = list(set(end_bas64))
        print("去重完毕！！去除",len(end_bas64) - len(end_bas64_A),"个重复节点")
        #永久订阅去除多余换行符
        bas64 = '\n'.join(end_bas64_A).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #试用去除多余换行符
        bas64_try = '\n'.join(end_try).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #获取时间，给文档命名用
        t = time.localtime()
        date = time.strftime('%y%m', t)
        date_day = time.strftime('%y%m%d', t)
        #创建文件路径
        try:
            os.mkdir(f'{update_path}{date}')
        except FileExistsError:
            pass
        txt_dir = update_path + date + '/' + date_day + '.txt'
        #写入时间订阅
        file = open(txt_dir, 'w', encoding='utf-8')
        file.write(bas64)
        file.close()       
        
        #减少获取的个数
        r = 1
        length = len(end_bas64_A)  # 总长
        m = 8  # 切分成多少份
        step = int(length / m) + 1  # 每份的长度
        for i in range(0, length, step):
            print("起",i,"始",i+step)
            zhengli = '\n'.join(end_bas64_A[i: i + step]).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
            #将获得的节点变成base64加密，为了长期订阅
            obj = base64.b64encode(zhengli.encode())
            plaintext_result = obj.decode()
            #写入长期订阅
            file_L = open("Long_term_subscription"+str(r), 'w', encoding='utf-8')
            file_L.write(plaintext_result)
            r += 1
        #写入总长期订阅
        obj = base64.b64encode(bas64.encode())
        plaintext_result = obj.decode()
        file_L = open("Long_term_subscription_num", 'w', encoding='utf-8')
        file_L.write(plaintext_result)
        #写入试用订阅
        obj_try = base64.b64encode(bas64_try.encode())
        plaintext_result_try = obj_try.decode()
        file_L_try = open("Long_term_subscription_try", 'w', encoding='utf-8')
        file_L_try.write(plaintext_result_try)
        #写入README
        with open("README.md", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        now_time = datetime.datetime.now()
        TimeDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for index in range(len(lines)):
            try:
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription_num`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription1`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription2`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription3`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription4`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription5`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription6`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription7`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription8`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length-step*7}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription3.yaml`\n': # 目标行内容
                    lines.pop(index+4)
                    lines.pop(index+4)
                    lines.insert(index+4, f'Updata：`{TimeDate}`\n')
                    lines.insert(index+4, f'### Try the number of high-speed subscriptions: `{len(try_sub)}`\n')
                if lines[index] == '>Trial subscription：\n': # 目标行内容
                    lines.pop(index)
                    lines.pop(index)
                """
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
                """
            except:
                #print("写入READ出错")
                pass
        #写入试用订阅
        for index in range(len(lines)):
            try:
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        #lines.insert(index+n-1, f'\n>')
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
            except:
                print("写入试用出错")
        
        with open("README.md", 'w', encoding='utf-8') as f:
            data = ''.join(lines)
            f.write(data)
        print("合并完成✅")
        try:
            numbers =sum(1 for _ in open(txt_dir))
            print("共获取到",numbers,"节点")
        except:
            print("出现错误！")
        
    return

#获取clash订阅
def get_yaml():
    print("开始获取clsah订阅")
    urls = []
    n = 1
    for i in urls:
        response = requests.get(i)
        #print(response.text)
        file_L = open("Long_term_subscription" + str(n) +".yaml", 'w', encoding='utf-8')
        file_L.write(response.text)
        file_L.close()
        n += 1
    print("clash订阅获取完成！")

#获取机场试用订阅
def get_sub_url():
    V2B_REG_REL_URL = '/api/v1/passport/auth/register'
    times = 1
    for current_url in home_urls:
        i = 0
        while i < times:
            header = {
                'Referer': current_url,
                'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            form_data = {
                'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))+'@gmail.com',
                'password': 'autosub_v2b',
                'invite_code': '',
                'email_code': ''
            }
            if current_url == 'https://xn--4gqu8thxjfje.com' or current_url == 'https://seeworld.pro'  or current_url == 'https://www.jwckk.top'or current_url == 'https://vvtestatiantian.top':
                try:
                    fan_res = requests.post(
                        f'{current_url}/api/v1/passport/auth/register', data=form_data, headers=header)
                    auth_data = fan_res.json()["data"]["auth_data"]
                    #print(auth_data)
                    fan_header = {
                        'Origin': current_url,
                        'Authorization': ''.join(auth_data),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Connection': 'keep-alive',
                        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                        'Referer': current_url,
                    }
                    fan_data = {
                        'period': 'onetime_price',
                        'plan_id': '1',
                    }
                    fan_res_n = requests.post(
                        f'{current_url}/api/v1/user/order/save', headers=fan_header, data=fan_data)
                    #print(fan_res_n.json()["data"])
                    fan_data_n = {
                        'trade_no':fan_res_n.json()["data"],
                        #'method': '1',
                    }
                    fan_res_pay = requests.post(
                        f'{current_url}/api/v1/user/order/checkout', data=fan_data_n, headers=fan_header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={fan_res.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as result:
                    print(result)
                    break
            else:
                try:
                    response = requests.post(
                        current_url+V2B_REG_REL_URL, data=form_data, headers=header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as e:
                    print("获取订阅失败",e)
            i += 1

            
  
def get_kkzui():
    # ========== 抓取 kkzui.com 的节点 ==========
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://kkzui.com/jd?orderby=modified",headers=headers)
        article_url = re.search(r'<h2 class="item-heading"><a href="(https://kkzui.com/(.*?)\.html)"',res.text).groups()[0]
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'<p><strong>这是v2订阅地址</strong>：(.*?)</p>',res.text).groups()[0]
        print(sub_url)
        e_sub.append(sub_url)
        print("获取kkzui.com完成！")
    except:
        print("获取kkzui.com失败！")
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://www.cfmem.com/search/label/free",headers=headers)
        article_url = re.search(r"https?://www\.cfmem\.com/\d{4}/\d{2}/\S+v2rayclash-vpn.html",res.text).group()
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'>v2ray订阅链接&#65306;(.*?)</span>',res.text).groups()[0]
        print(sub_url)
        try_sub.append(sub_url)
        e_sub.append(sub_url)
    except Exception as e:
        print(e)
        
    
if __name__ == '__main__':
    print("========== 开始获取机场订阅链接 ==========")
    get_sub_url()
    print("========== 开始获取kkzui.com订阅链接 ==========")
    get_kkzui()
    print("========== 开始获取频道订阅链接 ==========")
    for url in urls:
        #print(url, "开始获取......")
        thread = threading.Thread(target=get_content,args = (url,))
        thread.start()
        threads.append(thread)
        #resp = get_content(get_channel_http(url))
        #print(url, "获取完毕！！")
    #等待线程结束
    for t in tqdm(threads):
        t.join()
    print("========== 准备写入订阅 ==========")
    res = write_document()
    clash_sub = get_yaml()
    print("========== 写入完成任务结束 ==========")
