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

'http://1.1596666.xyz',
'http://1.1598888.xyz',
'http://103.70.59.53',
'http://146.56.101.50',
'http://2983839.xyz',
'http://2ec535a5c35aa5a4b44249428dbb3d01.52pokemon.top',
'http://372ae8252c9ce608c5f7066f2177dfb1.52pokemon.top',
'http://52.moguyun.xyz',
'http://54.193.243.32',
'http://569cdn.1010520.click',
'http://6465307854ab0a2c82b66d32ffa2107e.52pokemon.top',
'http://66ds.dishujichang.xyz',
'http://6b.zhunchuanpb.com',
'http://6bsub.zhunchuanpb.com',
'http://a123.buzz',
'http://ant77.top',
'http://api.123417.xyz',
'http://api.aca.best',
'http://api.scyu.xyz',
'http://api.sgjc.xyz',
'http://api.wtcloud.xyz',
'http://api.xn--14ra41gd24b.xyz',
'http://api-0609.m55u97uleod7lm5.download',
'http://app2024.jieshiwangluo.com',
'http://beautyandbeast.link',
'http://best.momoxiaodian.cc',
'http://bp.wbno1.xyz',
'http://c9k.buzz',
'http://cdn.fastwork.cc',
'http://chaojiji.one',
'http://config.sled.autos',
'http://dashabi.ping-zi-yun.icu',
'http://dishujichang.xyz',
'http://dy.changyouVPN.top',
'http://dy.changyouvpn.top',
'http://dy.hpyjc.top',
'http://dy.silicloud.xyz',
'http://dy.xyyjc.top',
'http://e8a580bd3a51b6050aabd8919a17d106.52pokemon.top',
'http://ec2-13-215-48-59.ap-southeast-1.compute.amazonaws.com',
'http://em7.buzz',
'http://fanqiang88.top',
'http://fbapiv1.fbsublink.com',
'http://fdgdr0dg3.xbvpn.vip',
'http://feigou.zhunchuanpb.com',
'http://fs123121.cdn.22.jiacdnd123456789.com',
'http://gbtgurl01.org',
'http://ggiuwegivhe123.a123.bond',
'http://guguyun.xyz',
'http://hpyjc.top',
'http://jjz.31465.cfd',
'http://jshou.top',
'http://lafusees.com',
'http://laobideng.xyz',
'http://lianjiasub.work',
'http://ly.ccwink.cc',
'http://mf.kejifan88.top',
'http://mine.subcsyun.online',
'http://msvpn.gougouvpn.xyz:88',
'http://n15uvht4r659107p.eastasia.cloudapp.azure.com',
'http://nachoneko.cn',
'http://nangang.mom',
'http://on1vejas4m6z.w7yxefcx0i11.click',
'http://one.bblinks.top',
'http://panda.xn--i8sx78aisa52z.com',
'http://panda.xn--lbrx91akmhm30c.com',
'http://s.33y.run',
'http://s.kalaa.me',
'http://s1.subcsyun.online',
'http://s3.subcsyun.online',
'http://s4.subcsyun.online',
'http://saobiwang.top',
'http://sp.nfsq.me',
'http://sub.expmc.com',
'http://sub.sub.sub.subsub123456789.com',
'http://sub.xn--54qu5qypuo1o.xn--fiqs8s',
'http://sub1.efshop.cc',
'http://sub2086.fnyune.shop:2086',
'http://subs.202218.xyz',
'http://tuzi226.top',
'http://url.lx-cloud.xyz',
'http://user.dafeiji.one',
'http://user.tsunaminet.cc',
'http://v2.fkc99m.cfd',
'http://v2-1.806cms.top',
'http://vip.365cloud.me',
'http://vpn.gougouvpn.xyz:88',
'http://vps.huanshi88.sbs',
'http://www.chachajichang.top',
'http://www.crosswall.org',
'http://www.fanqiang88.top',
'http://www.freeflyingcloud.xyz',
'http://www.mmsbs.buzz',
'http://www.pingzicloud.top',
'http://xn--4gq62f8yih87b.site',
'http://xn--gmqa02ag57d.com',
'http://xn--mesx48ahb331x.com',
'http://xxxu.xyz',
'http://ya555.top',
'http://yy-cmi.mozhiti.top',
'http://yzxxy.top',
'https://01.laomao1.xyz',
'https://03.laomao1.xyz',
'https://04.laomao1.xyz',
'https://0415.chun-auto-one.xyz',
'https://06.laomao1.xyz',
'https://069059b7ef-1ytapi01.1ytsub.com',
'https://07.laomao1.xyz',
'https://08.laomao1.xyz',
'https://088ea81a-3547-85e0-4af6-dfcb3c6674aa.372372.xyz',
'https://088EA81A-3547-85E0-4AF6-DFCB3C6674AA.372372.xyz',
'https://0918bde2-d3c6-354c-9919-672626903188.nginxtanz.click',
'https://0b96e976-9ec3-44c0-aa2b-30bf8b0792ea.com',
'https://0d2th.no-mad-world.club',
'https://0f36b897-2a77-3921-a2ca-3d1bb29fa8a5.ftqconfig.com',
'https://0mv.top',
'https://1.ayouok.online',
'https://1.baobaodeshanye.site',
'https://1.bethebest.eu.org',
'https://1.cutecloud.net',
'https://1.ovofast.xyz',
'https://1.xn--xc3ao8r.top',
'https://10th.sub-airport.com',
'https://11.laomao1.xyz',
'https://1122331.xyz',
'https://12.laomao1.xyz',
'https://12123.org',
'https://13.laomao1.xyz',
'https://1321078938-11mmjf3qkb-hk.scf.tencentcs.com',
'https://135841.xyz',
'https://14.laomao1.xyz',
'https://14ce7f2b-1b99-417c-ab7b-6de0d94baec8.apcdn.org',
'https://15.laomao1.xyz',
'https://16th.sub-airport.com',
'https://17.laomao1.xyz',
'https://17852.xyz',
'https://18.laomao1.xyz',
'https://196284.nginxzfd.xyz',
'https://1a1fe884-ae3c-3610-8075-cb778431f722.subdog.cyou',
'https://1milk.top',
'https://1st.sub-airport.com',
'https://1ytcom01.1yunti.net',
'https://2.maomaody.xyz',
'https://20.laomao1.xyz',
'https://20189999.xyz',
'https://2024.175698.xyz',
'https://20240802.canadapost-vip.com',
'https://209966.xyz',
'https://22.lownet.xyz',
'https://231787.xyz',
'https://25054128.xyz',
'https://3.feiniaoyun01.life',
'https://3.mimoe4.ru',
'https://30178aeb-8299-045d-fb67-ae12ce73dd2c.buou.lol',
'https://30388d70-6f5c-4d7c-8daa-9d3df7c5c526.9150e878-8296-4798-a172-c3fe66b8dee5.ddnsgeek.com',
'https://3093492f6b2332f8server.lycoris.one',
'https://32v.xyz',
'https://33.maoyun1.shop',
'https://333333.live',
'https://353g78qgfq.surfcat.store',
'https://38.181.25.67',
'https://3h.lv',
'https://4.jdy1027ue.lol',
'https://404.k6.gay',
'https://41be350f-5079-4195-8329-f6fa25f9906a.com',
'https://422.jcool.cool',
'https://4259f1e1-ff0e-461a-b7ff-c734d374eb68.shandiannginx.com',
'https://45bcb080ade759e2.cdn.jiashule.com',
'https://47.237.21.85',
'https://4e60bafd-0633-4e8d-a02a-eef51cd1ad8e.xn--mes358a.art',
'https://4gfree.asia',
'https://4th-subscription-from-chickenfarmer.top',
'https://4ulgur4.wuxianliuliang.cfd',
'https://5.52vpn.xyz',
'https://502dy.cloudoo.xyz',
'https://520.qjfjc.top',
'https://523qaweg246.pandafly.site',
'https://52daishu.uk',
'https://52niu.xyz',
'https://52pokemon.xz61.cn',
'https://548ff3c1-d8c8-3110-a65a-fb55573380c7.nginx24tanz.xyz',
'https://569cdn.1010520.click',
'https://57e6938f-92e3-3e4c-ad9d-6c8622486768.nginx24zfd.xyz',
'https://711.886511.xyz',
'https://7cd49968.nmsubs.com',
'https://7th-subscription-from-chickenfarmer.top',
'https://805678.xyz',
'https://8payj.no-mad-world.club',
'https://9527.bigbigwatermelon.com',
'https://98kjc.com',
'https://99ding.men',
'https://9th-subscription-from-chickenfarmer.top',
'https://a.1145149.xyz',
'https://a.aikllc.tech',
'https://a.fsyun.xyz',
'https://a.jiedianxielou.workers.dev',
'https://a.mtdwoodwork.com',
'https://a.qcsub.com',
'https://a.qcsub.top',
'https://a.s2cat.cc',
'https://a.sdwan.im',
'https://a.suixincloud.top',
'https://a.xn--mnqr2d776chcv.com',
'https://a01.wjyhalou.makeup',
'https://a1.8jiasu.com',
'https://a2.shidianban.top',
'https://a241219.888545.xyz',
'https://a76.aaa7.info',
'https://a94d418e-1898-42df-bcf2-d970a5f3a939.mysubsoft.com',
'https://aaa.us123.icu',
'https://aaa.yunduanjc.top',
'https://abqmygfu.mdssconfig.com',
'https://abyssvpnya.net',
'https://ac1f3b35-1d03-3a85-beab-258d8f23edc6.nginxdotu.xyz',
'https://ac59a7cd-11af-3e35-a098-b785688ec627.aliyunsub.com',
'https://a-cdn.b-cdn.net',
'https://acl.syyn.pw',
'https://acow.wtf',
'https://admin.xn--iiq451n.com',
'https://adtzwnkwqq.southeastasia.cloudapp.azure.com',
'https://ae86.235999.xyz',
'https://af078381-fcf9-457a-b03a-7bfaf506cd0b.xn--l6qx3lcvp58x.com',
'https://agit.ai',
'https://ahiddenmask.top',
'https://aicccc.top',
'https://aifun.trafficmanager.net',
'https://aigame.totwo.xyz',
'https://aiosjhdy.forbit-api.boats',
'https://airport.raloar.top',
'https://aliair.xyz',
'https://alpha.sagittarius-link.com',
'https://amatrixap.com',
'https://anydoor.xyz',
'https://aoop.top',
'https://ap.niaodi.top',
'https://ap.niubi.site',
'https://apexxy.top',
'https://api.911tg3rs.com',
'https://api.abyssyun.top',
'https://api.acaisbest.shop',
'https://api.aurapro.xyz',
'https://api.cn2.pw',
'https://api.dingyueapi.cc',
'https://api.dingyueddns.life',
'https://api.e687699.top',
'https://api.e986532.top',
'https://api.eflink.xyz',
'https://api.fenghuolun.xyz',
'https://api.flowercloud.xyz',
'https://api.fuckvps.net',
'https://api.fuckyun.cc',
'https://api.georgle.cyou',
'https://api.heima2u.com',
'https://api.hk03.fysub.com',
'https://api.ikuntool.com',
'https://api.inforun.work',
'https://api.ktcat.online',
'https://api.lendcloud.tech',
'https://api.meomiao.me',
'https://api.misakanet.buzz',
'https://api.nainiucloud.xyz',
'https://api.neigui.us.kg:443',
'https://api.nexconvert.com',
'https://api.nutbit-node.lat',
'https://api.oxygenproxy.top',
'https://api.pithecia.com',
'https://api.shin-x.top',
'https://api.ssrsub.com',
'https://api.sub-200.club',
'https://api.tshl.cc',
'https://api.tsutsu.one',
'https://api.wcc.best',
'https://api.wd-blue.com',
'https://api.wd-red.com',
'https://api.wtcloud.xyz',
'https://api.xinyo.vip',
'https://api.xjichang.buzz',
'https://api.xmancdn.net',
'https://api.xn--14ra41gd24b.xyz',
'https://api.xn--bnq37rc0nw50b.com',
'https://api.xn--yfr72t8r4bvhd.xyz',
'https://api.xqc.best',
'https://api.xyurl.site',
'https://api.ytoo.xyz',
'https://api.yuyan.vin',
'https://api.zuanshivpn.cn',
'https://api.zzzzzl.me',
'https://api03.cjpaoche.xyz',
'https://api1.441166.xyz',
'https://api1.xn--bnq37rc0nw50b.com',
'https://api2.mbo-xxx.top',
'https://api2.xn--bnq37rc0nw50b.com',
'https://api3.6yuan.top',
'https://api3.okaycloud.top',
'https://apidy.pqjc.site',
'https://apii.xqc.best',
'https://apinainiucloud.lat',
'https://api-subscribe.lycoris.cam',
'https://apiv1.v27qae.com',
'https://apiv2.lemongg.top',
'https://api-zz.xn--14ra41gd24b.xyz',
'https://app.100861234.xyz',
'https://app.cloudlion.me',
'https://app.gomeow.cloud',
'https://app.jisovpn.site',
'https://app.lwjyj.com',
'https://app.mitce.com',
'https://app.zilihaijichang.top',

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
