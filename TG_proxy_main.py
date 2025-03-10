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
'https://qlvpn.net',
'https://badsd.com',
'https://qingyuntipro.com',
'https://www.westworldvpn.net',
'https://ikunvpn.cc',
'https://flyingbirds.cc',
'https://vilavpn.net',
'https://www.pandajiasu.com',
'https://nexitally.one',
'https://www.aoxspeed.com',
'https://一元.org',
'https://www.catbucket.cn',
'https://mojie.app',
'https://apps.microsoft.com',
'https://ibale.co',
'https://xiaojicf.com',
'https://v2.xiaojikp.cc',
'https://xiaoniukeji.cc',
'https://奈云机场.com',
'https://加速啦机场.com',
'https://goj.app',
'https://lantern.io',
'https://zhuanlan.zhihu.com',
'https://hide.mn',
'https://xbsj9728.space',
'https://www.leiting.io',
'https://fscloud111.gitbook.io',
'https://大机场.net',
'https://1yunti.org',
'https://xj-speed.com',
'https://www.ggkuai.com',
'https://goflyvpn.com',
'https://balecc.com',
'https://web.fscloud.cc',
'https://b.ikunvpn.com',
'https://www.蓝帆云.com',
'https://haita.io',
'https://purejiasuqi.com',
'https://m.wawaapp.net',
'https://pandavpnpro.com',
'https://us.oteacc.org',
'https://docs.reizs.cyou',
'https://jpcdn.ts123.cc',
'https://app.fanqiev2.work',
'https://baijiahao.baidu.com',
'https://www.skylinevpn.net',
'https://ltss.pro',
'https://portal.colacloud.net',
'https://hacksg.com',
'https://console.qlvpn.com',
'https://www.bilibili.com',
'https://reijiasu.cc',
'https://xbsj5632.website',
'https://shandianpro.com',
'https://sd.369.cyou',
'https://aha-speed.net',
'https://www.golink.com',
'https://net.balala.lol',
'https://analku.com',
'https://ltss.cc',
'https://mistycloud.io',
'https://dash.lemoncloud.cyou',
'https://dog.ssrdog.com',
'https://download.easylinkvpn.com',
'https://iklyun.com',
'https://www.lets-connect-always.com',
'https://justmysocks.cn.com',
'https://falemon.com',
'https://lajichang.eu',
'https://fliggycloud.org',
'https://t.me',
'https://www.biubiu.tw',
'https://www.apricot.red',
'https://flowercloud.net',
'https://ovofast.com',
'https://dtcloud.us',
'https://microsoftedge.microsoft.com',
'https://dlercloud.cc',
'https://xsus.wiki',
'https://www.telescope.name',
'https://www.189.cam',
'https://www.skylinevpn.com',
'https://www.v2ny.com',
'https://v2.nanoport.xyz',
'https://www.letsvpn.im',
'https://www.baiyuncloud.cc',
'https://www.arr.network',
'https://citrus.gitbook.io',
'https://www.leiting.lol',
'https://www.bcfdm.com',
'https://v2.tankecloud.me',
'https://socloud.cc',
'https://www.rockyhsu.com',
'https://tolink.pro',
'https://antvpn-proxy.iceberg-studio.com',
'https://www.godualnet.com',
'https://dhh.app',
'https://cs.zhvpn.com',
'https://marslink.org',
'https://mars.369.cyou',
'https://www.zhihu.com',
'https://mojie.me',
'https://www.789jiasu01.com',
'https://m5.juanwang001.online',
'https://www.chuansuovpn.com',
'https://colacloudnet.com',
'https://www.abruning.com',
'https://www.dotsvpn.com',
'https://bajie.pw',
'https://rabbitpro.app',
'https://techmusea.com',
'https://极速时代.com',
'https://www.1day.sbs',
'https://www.axjsq.com',
'https://bywa-1.art',
'https://www.dukadi.one',
'https://www.chuansuovpn.net',
'https://sslinkcn.com',
'https://xhjfq.com',
'https://ss.mba',
'https://www.jfyun1.com',
'https://web3vpn.net',
'https://candy2.top',
'https://imginn.com',
'https://2yuan-airport.com',
'https://www.ermao.net',
'https://getmalus.com',
'https://www.laowangxz.com',
'https://cave99.com',
'https://bajie.ac',
'https://proxyium.com',
'https://xqcloud.net',
'https://pj.telescope.name',
'https://apanel.tinnyrick.com',
'https://www.cyberghostvpn.com',
'https://jiasu91.com',
'https://www.letsvpn.world',
'https://netvpn.cc',
'https://www.reddit.com',
'https://reborn.kaochang.ltd',
'https://nicecloud.co',
'https://www.xhjfq.com',
'https://dash.fscloud.cc',
'https://www.mozilla.org',
'https://www.xiyouip.com',
'https://shuttle.gt-all.com',
'https://www.09axjsq.com',
'https://www.98kjsq.com',
'https://mojie.la',
'https://www.gsou.link',
'https://www.ssr-vpn.com',
'https://geph.io',
'https://www.cryxr.com',
'https://tapfog.com',
'https://english.yunnan.cn',
'https://www.laomaovpn.vip',
'https://nbswarm.org',
'https://bygcloud.com',
'https://zx1.lbjsu.com',
'https://www.quickq.io',
'https://one.one.one.one',
'https://skystars.top',
'https://www.qiuyinjsd.com',
'https://slowerssr.com',
'https://mccloud.gay',
'https://greasyfork.org',
'https://nutsvpn.tech',
'https://order.yizhihongxing.org',
'https://hidemy.io',
'https://x.com',
'https://wd-cloud.net',
'https://gkd.buzz',
'https://dynamite11.com',
'https://privadovpn.com',
'https://wmsxwd.org',
'https://proxyhub.me',
'https://lbjsu.com',
'https://vip.tinnyrick.com',
'https://www.f2ray.com',
'https://t.xcvpn.us',
'https://7777711.xyz',
'https://paoche.ga',
'https://www.xiyouweb.net',
'https://kako.高中生网.com',
'https://smjcdh.com',
'https://www.youtube.com',
'https://www.leidianjiasu.com',
'https://慈善机场.com',
'https://bbxy.浙地珠宝.com',
'https://52lanmao.com',
'https://www.plexvpn.pro',
'https://targettrend.com',
'https://www.sdvpn.app',
'https://www.ucjiasuqi.com',
'https://beibeicloud.shop',
'https://g.nga.cn',
'https://ss-id.com',
'https://tjjj.xyz',
'https://dongligang.me',
'https://www.dragonvpn.cc',
'https://www.freedidi.com',
'https://www.xuanfengvpn2.net',
'https://www.xiosin.com',
'https://www.totocloud.com',
'https://b.antss.me',
'https://sjiasu.com',
'https://www.haiou09.com',
'https://xpoti.com',
'https://socloud.me',
'https://金坷垃.com',
'https://jgjs02.com',
'https://mogu24.com',
'https://www.letsconn.com',
'https://www.dotsvpn1.com',
'https://www.v2qc.com',
'https://a.yunxi.app',
'https://www.heibaoapp.net',
'https://go.milai.org',
'https://www.easylinkvpn.com',
'https://www.nthu1.com',
'https://www.tanzcloud.com',
'https://to.flyintpro.com',
'https://www.firefox.net.cn',
'https://www.lt25.cc',
'https://翻墙机场.com',
'https://www.08axjsq.com',
'https://www.skyline.plus',
'https://rusuos.com',
'https://web.bananaspeed.team',
'https://www.xiyovpn.com',
'https://echonetwork.club',
'https://newhua99.com',
'https://wzpwmu.com',
'https://www.realnode.info',
'https://www.qingzhou.world',
'https://qzhome.cc',
'https://www.有连.com',
'https://www.greenjsd.com',
'https://milfall.com',
'https://jfcat.net',
'https://www.qlvpn.com',
'https://vpnreview.com.tw',
'https://getyuuttojiasuqi.com',
'https://access.ftqnet.com',
'https://wolongleyou.com',
'https://huacloud.dev',
'https://www.maulusvpn.com',
'https://in.mesl.cloud',
'https://feitan.me',
'https://zhshi.gitlab.io',
'https://zx2023.cc',
'https://haiou03.com',
'https://www.zerocloud.works',
'https://gatern.com',
'https://www.hx666.info',
'https://91unicorn.cloud',
'https://www.bjchuhai.com',
'https://haigui1.com',
'https://anyland01.com',
'https://www.speedin.com',
'https://qiuyin.app',
'https://auroravpnapp.com',
'https://tagss04.pro',
'https://flyingbird.pro',
'https://shanhai.me',
'https://fastestcloud.xyz',
'https://fastlink.ws',
'https://www.mydown.com',
'https://v2.quanstring.top',
'https://www.naiun.top',
'https://by.kokoro88.top',
'https://a.chuanshiqi.top',
'https://www.fastlink.pro',
'https://www.jnaku.com',
'https://极速官网.com',
'https://www.mg188online.com',
'https://ikuuu.org',
'https://www.downgo.cn',
'https://v.xdy2.vip',
'https://www.sixfast8.com',
'https://j8doba2sodptvzprvmcb.wgetcloud.org',
'https://starlink.to',
'https://star.369.cyou',
'https://www.miyun.la',
'https://www.mayijiasd.com',
'https://hitun.io',
'https://www.okss.us',
'https://qiuyin.co',
'https://www.gogonetpas.net',
'https://mojie.nl',
'https://chwy.niedzfs.com',
'https://tagss01.pro',
'https://tagss02.pro',
'https://caiyun.pro',
'https://uu.163.com',
'https://ftzaffcom01.fliggyaff.xyz',
'https://nexitally.com',
'https://hidemyname.io',
'https://nordwangluo.com',
'https://worldtz.com',
'https://rs1s.com',
'https://dog.ssrdog111.com',
'https://www.jichang.pro',
'https://watermelon.besnow.me',
'https://hsyun.t767.cn',
'https://news.jxcn.cn',
'https://www.nutbit.net',
'https://www.qiaoyadi.com',
'https://www.dlairport.com',
'https://v2.fastlink-aff02.com',
'https://beibeilink.top',
'https://www.chainuk.top',
'https://juzicloud.net',
'https://性价比机场.net',
'https://www.amytele.net',
'https://portal.wl-site4.com',
'https://大白机场.com',
'https://www.tsbyxcx.com',
'https://zerocloud.works',
'https://kerrynotes.com',
'https://www.kuaigou.life',
'https://www.kobocity.com',
'https://www.sogou.com',
'https://www.jamesdailylife.com',
'https://feijiyun889.net',
'https://blog.xinmedia.com',
'https://go.51tz.cc',
'https://wwz.lanzoul.com',
'https://huojian.02000.net',
'https://appparapc.com',
'https://get.kissiya.com',
'https://telegramchannels.me',
'https://support.xwhales.monster',
'https://feijichang.org',
'https://www.saraba1st.com',
'https://bbs.gamersky.com',
'https://www.hdvrar.com',
'https://一元机场.com',
'https://tyty.club',
'https://qingyun.io',
'https://qingyunjia.cc',
'https://ad.adgn.work',
'https://www.paopao.dog',
'https://ppg.369.cyou',
'https://www.jimmm.club',
'https://www.qianglie.com',
'https://熊云机场.com',
'https://shin-x.top',
'https://user.tf06.com',
'https://dftcraft.com',
'https://bixiny.com',
'https://vpn15.top',
'https://tryfqtzapp.com',
'https://clashvpn.net',
'https://discordvpn.com',
'https://doladder.com',
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
