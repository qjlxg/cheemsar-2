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

'https://ap.niubi.site',
'https://api-hx.02000.net',
'https://api-qw.02000.net',
'https://api-zz.xn--14ra41gd24b.xyz',
'https://api.1vpn.sbs',
'https://api.abyssyun.top',
'https://api.acaisbest.shop',
'https://api.bigme.online:8211',
'https://api.e687699.top',
'https://api.e986532.top',
'https://api.fanss.vip',
'https://api.fenghuolun.xyz',
'https://api.fuckvps.net',
'https://api.fuckyun.cc',
'https://api.heima2u.com',
'https://api.hy2.lol',
'https://api.otcopusvpn.cc:18008',
'https://api.pithecia.com',
'https://api.prprcloud.life',
'https://api.ssrsub.com',
'https://api.touhou.center/sub',
'https://api.tshl.cc',
'https://api.xinyo.vip',
'https://api.xn--14ra41gd24b.xyz',
'https://api.xn--y20az5i.xyz',
'https://api.xn--yfr72t8r4bvhd.xyz',
'https://api.xqc.best',
'https://api.xtt777.com',
'https://api.xyurl.site',
'https://api.ymvpnpro.cc:8700',
'https://api.zzzzzl.me',
'https://api03.cjpaoche.xyz',
'https://api1.441166.xyz',
'https://api1.danidapigu.top',
'https://api1.fzdwf.top',
'https://api1.okaycloud.top',
'https://api1.xn--bnq37rc0nw50b.com',
'https://api2.mbo-xxx.top',
'https://api2.okaycloud.top',
'https://api2.xn--bnq37rc0nw50b.com',
'https://api3.6yuan.top',
'https://api7.6yuan.top',
'https://apiceshi.51alibaba.top',
'https://apidy.pqjc.site',
'https://apisub.mcwy.xyz',
'https://apisudunw.sudunv.com',
'https://apiv2.lemongg.top',
'https://apiv2.lipulai.com',
'https://apopcloud.com',
'https://app.cloudlion.me',
'https://app.gomeow.cloud',
'https://app.jisovpn.site',
'https://app.legeth.cc',
'https://app.lwjyj.com',
'https://app.tline.website',
'https://aq.louwangzhiyu.xyz',
'https://artislg.com',
'https://artislg.com/api',
'https://asa.lol',
'https://asa01.888545.xyz',
'https://asa035.888545.xyz',
'https://asdf.888545.xyz',
'https://atacyun.yydsii.com',
'https://atong88.top/klBrvxTYgGdWoqF0cLRi4AS93S',
'https://auth.newlikebooks.xyz',
'https://awacloud.online',
'https://b.jiedianxielou.workers.dev',
'https://b.xiaow.cc',
'https://b27479ca-869b-4d02-9e53-a3d6d7785d13.nginxmdss.xyz',
'https://baigou.kkhhddnn.cn',
'https://bajie.info',
'https://bajie.xyz',
'https://bansub7.bplink.xyz',
'https://bansub8.bplink.xyz',
'https://base64.bigwatermelon.org',
'https://bat.fcbjw.com',
'https://bav46z6c.nicecloud.win:8443',
'https://bayoeorescentpossessicoanseparateuneforescenphocommitte.adoptangelaboradvacotionclwonthorughconfrmcompimentdeseertaltar.org',
'https://bb.jmvks.cn',
'https://bbg.bbgjc.cc',
'https://bbgjc.cc',
'https://bbjc.xyz',
'https://bdsafhh.yiyuanlx.cc',
'https://bengalj.com',
'https://blueAir.colacloud.free.hr',
'https://board.nsde.date',
'https://board.queqiao.online',
'https://boou.colacloud.free.hr',
'https://bozhi.591haoka.com',
'https://bpjc.lol',
'https://bptz.xyz',
'https://bunnyspeedox.online',
'https://butppo.473221.xyz',
'https://bxy.re',
'https://c.066664.xyz',
'https://c3.notesync.org',
'https://c4.notesync.org',
'https://cainiao164.top',
'https://cainiao172.top',
'https://cainiaofit.cc',
'https://cat.ikkt.cn',
'https://cdn-web-api.moeu.top',
'https://cdn.1454250.xyz',
'https://cdn.fraternizey.com',
'https://cdn.qfyun.me',
'https://cdn.wumaojichang.com',
'https://cdn1.xr56385d.qianglie.cloud',
'https://cdn1711437153.ppgnginx.com',
'https://cdn1712594108.ppgnginx.com',
'https://cdn1715497317.ppgnginx.com',
'https://cdnbao.foxi4.com',
'https://cedb4ccc-89b7-3a24-962c-ea8f65b11deb.aliyunsub.com',
'https://ceshi.888451.xyz',
'https://cf.7854128.xyz',
'https://cf.lemshow.top',
'https://cf.loveqyun.cyou',
'https://cfj.chuifengji.top',
'https://cfyun.top',
'https://cfyun01.sbs',
'https://chaozhijc.xyz',
'https://checkhere.top',
'https://chiguayun.pro',
'https://china.huawei-cloud.shop',
'https://citi.terminal69.win',
'https://ck2.yunxiangvip.mom',
'https://cloud.anyijc.top',
'https://cloud.asdkd.top',
'https://cloud.chaozhijc.xyz',
'https://cloud.gomeow.tech',
'https://cloud.gyyun.top',
'https://cloud.jsfx.tech',
'https://cloud.optionwiney.com',
'https://cloud.xjyjc.top',
'https://cloud.ykkk.tech',
'https://cloud.yydschina.top',
'https://cloudcat.top',
'https://cloudflaresub.yuwan.link',
'https://cloudlion.me',
'https://cm.qc77.cn',
'https://cococloud.online',
'https://cokecloud.net',
'https://config.huojian111.com',
'https://csgo.fask511.cfd',
'https://csgo1.fask511.cfd',
'https://cshjc.xz61.cn',
'https://csicd782-isu.acyunv.buzz',
'https://csyun.t1csyun.shop',
'https://cyberguard.cfd',
'https://d.palu123.com',
'https://d.waka.plus',
'https://d1.dlsdist.net',
'https://d1to2me5cb4qc0.cloudfront.net',
'https://d2f42a86-2a1f-49b5-bd2f-d2154daa6a09.com',
'https://d3keb6jjtp861e.cloudfront.net',
'https://d57761d6-e86d-4f55-9a5d-aece8a55cc26.xn--mes358a.art',
'https://dadada.acaisbest.com',
'https://dash.djjc.cfd',
'https://dash.ftclashcloud.mom',
'https://dash.pqjc.site',
'https://dash.yfjc.xyz',
'https://datacenter_us.pithecia.com',
'https://datmicxg.mdssconfig.com',
'https://dawson0207.xn--3iq226gfdb94q.com',
'https://daxun.buzz',
'https://dd.csjc.win',
'https://dd.moonriver.cfd',
'https://dd.xz61.cn',
'https://ddd.trc20.top',
'https://df810594c639v.cloudfront.net',
'https://dfgsdfg.ghkjfgjkdfghrjfghjvbnm.cfd',
'https://dingyue.trojanws.xyz',
'https://dingyue.wenlianyun.vip',
'https://dingyue.xxss.org',
'https://dingyue1.b-cdn.net',
'https://dj.taipeicity.news',
'https://djjc.cfd',
'https://dkcc71fg830ah.cloudfront.net',
'https://dl.owokkvsxks.store',
'https://dl.vfkum.website',
'https://doata.net',
'https://doucat.top',
'https://douyun.sbs',
'https://duijie.cfyun.top',
'https://duijie.pingziyun.top',
'https://dump.facal.one',
'https://dxapp.jmvks.cn',
'https://dy-1.smjcdh.com',
'https://dy.chaozhijc.xyz',
'https://dy.jntm.ikun.moshen.tech',
'https://dy.kuailejc.xyz',
'https://dy.kunkun.v6.navy',
'https://dy.magicm.link',
'https://dy.naisicloud.xyz',
'https://dy.netfly.sbs',
'https://dy.pmy666.xyz',
'https://dy.qjfjc.top',
'https://dy.shihuijeidian.xyz',
'https://dy.smjc.top',
'https://dy.ssysub6.xyz',
'https://dy.tagsub.net',
'https://dy.tgmini.top',
'https://dy.tsmpi.xyz',
'https://dy.ucat.live',
'https://dy.yh13.xyz',
'https://dy0.mmydy.xyz',
'https://dy01.mmydy.xyz',
'https://dy1.hhyun.in',
'https://dy1.mmydy.xyz',
'https://dy2.mmydy.xyz',
'https://dy3.yunhu1.xyz',
'https://dy4.mmydy.xyz',
'https://dy5.mmydy.xyz',
'https://dy513.mmydy.xyz',
'https://dy6.mmydy.xyz',
'https://dy7.mmydy.xyz',
'https://dy9.mmydy.xyz',
'https://dyapp123.355m.cn',
'https://dycd.gsjc.sbs',
'https://dycd.knjc.cfd',
'https://dydz.csjc.win',
'https://dydz.xn--mesv8bx6xtx3b.com',
'https://dylj.wanwan1024.top',
'https://dyvip.ianong.cn',
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
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription_num`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription1`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription2`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription3`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription4`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription5`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription6`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription7`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription8`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length-step*7}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription3.yaml`\n': # 目标行内容
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
