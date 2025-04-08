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

'https://154.21.202.201',
'http://sub.clashcat.cc',
'https://67.21.85.237',
'https://123kpl456.top',
'http://123kpl456.top',
'http://123vvv456.one',
'http://123yes456.rest',
'https://123yes456.rest',
'https://123vvv456.one',
'https://cc1.123kpl456.top',
'https://www.123xxx456.vip',
'http://r1icl0a.123yes456.rest',
'http://thesyeec7l60ouav1lz0tesk.top',
'https://r1icl0a.123yes456.rest',
'http://0lok71ok.123vvv456.one',
'https://0lok71ok.123vvv456.one',
'http://cc1.123kpl456.top',
'https://141.195.113.57',
'http://www.ucc117.one',
'https://www.ucc117.one',
'http://205.198.64.9:2096',
'https://console.qlvpn.com',
'https://ucc117.one',
'http://52.229.202.18',
'https://www.wolun8.com',
'http://20.2.155.198',
'http://45.32.11.125',
'https://23.172.40.113',
'https://wolun002.chaosu202501.com',
'http://www.hssl8088.icu',
'https://www.hssl8088.icu',
'https://hssl8088.icu',
'http://xx.qitech.site',
'https://xx.qitech.site',
'http://sl.sltech.cc',
'https://sl.sltech.cc',
'http://45.149.204.88:82',
'http://52.187.5.203',
'https://52.163.119.149',
'https://8.218.117.120',
'https://192.3.24.121',
'https://154.17.5.40',
'https://142.171.83.99',
'https://52.187.5.203',
'https://103.97.200.87',
'https://205.198.64.112',
'https://107.172.144.75',
'https://88.skyshops.net',
'http://88.tiankong.shop',
'http://88.tiankong.best',
'http://8.tiankong.shop',
'https://88.tiankong.best',
'http://8.tiankong.best',
'https://mmiaomiaomia-oss-cn-hongkon.shanhai.me',
'http://app.shanhai.me',
'https://65.75.209.206',
'https://app.shanhai.one',
'http://8.217.159.40',
'http://4t4.icu',
'http://tiankong-888.17788.xyz',
'http://888.tiankong.best',
'https://8.tiankong.best',
'http://88.skyshops.net',
'https://88.tiankong.shop',
'https://tiankong-888.17788.xyz',
'http://888.tiankong.shop',
'http://8.tkzc.shop',
'https://52.163.62.85',
'https://888.tiankong.shop',
'https://wjyhalou.makeup',
'https://888.tiankong.best',
'https://8.tkzc.shop',
'http://bbb.wolun999.com',
'https://bbb.chaosu444.com',
'http://aaa.wolun444.com',
'https://bbb.wolun999.com',
'https://bbb.wolun555.com',
'https://c.wolun444.com',
'http://ccc.chaosu555.com',
'https://aaa.chaosu444.com',
'https://bbb.wolun6.com',
'http://bbb.wolun555.com',
'http://c.chaosu444.com',
'http://bbb.chaosu333.com',
'http://bbb.wolun8.com',
'http://c.wolun7.com',
'http://aaa.chaosu222.com',
'http://aaa.wolun6.com',
'http://bbb.chaosu777.com',
'http://bbb.chaosu222.com',
'https://ccc.chaosu333.com',
'http://c.wolun555.com',
'http://c.wolun999.com',
'http://c.chaosu222.com',
'https://aaa.wolun999.com',
'https://ccc.chaosu444.com',
'https://bbb.wolun444.com',
'https://c.chaosu222.com',
'http://bbb.wolun444.com',
'https://bbb.wolun7.com',
'https://aaa.wolun555.com',
'http://aaa.wolun555.com',
'http://bbb.wolun6.com',
'https://bbb.chaosu555.com',
'http://aaa.chaosu777.com',
'https://c.chaosu777.com',
'https://c.chaosu666.com',
'http://bbb.chaosu555.com',
'https://bbb.chaosu333.com',
'https://bbb.chaosu222.com',
'https://aaa.wolun7.com',
'https://c.wolun7.com',
'http://c.chaosu777.com',
'http://ddd.chaosu333.com',
'https://bbb.wolun8.com',
'http://c.wolun6.com',
'https://aaa.chaosu222.com',
'https://m.chaosu111.com',
'https://aaa.wolun444.com',
'http://aaa.wolun999.com',
'http://c.wolun444.com',
'http://bbb.wolun7.com',
'https://c.chaosu444.com',
'https://ccc.chaosu555.com',
'https://c.chaosu555.com',
'https://47.239.135.167',
'https://52.229.202.18',
'http://app.shanhai.one',
'http://mmiaomiaomia-oss-cn-hongkon.shanhai.me',
'https://app.shanhai.me',
'https://shanhai.one',
'http://52.163.94.66',
'https://dmit.xinsi.us',
'http://154.21.202.201',
'https://almadafitsisetubaloubuavoro.oujiangbu.ovh',
'http://106.52.193.147',
'https://c.wolun6.com',
'https://ddd.chaosu333.com',
'https://c.wolun999.com',
'https://aaa.wolun8.com',
'http://aaa.chaosu444.com',
'http://bbb.chaosu444.com',
'http://aaa.wolun8.com',
'http://ccc.chaosu444.com',
'http://c.chaosu555.com',
'http://45.145.72.139',
'http://142.171.83.99',
'https://kao.1880671.xyz',
'http://kao.1880671.xyz',
'https://xk9401fj.5201874.xyz',
'http://xk9401fj.5201874.xyz',
'http://65.75.209.206',
'http://52.163.119.149',
'http://27.25.147.251',
'http://c.chaosu666.com',
'http://ccc.chaosu333.com',
'https://aaa.wolun6.com',
'http://aaa.wolun7.com',
'http://51.254.44.34:7001',
'https://94.74.106.187',
'https://www.yuanqitusi.com',
'https://8.217.159.40',
'http://6.yaoyaojs1.shop',
'https://wolun003.chaosu202501.com',
'https://www.kuaileixingxi.cc',
'https://www.kuaileigo.cc',
'https://6.yaoyaojs1.shop',
'http://6.ccyy01.shop',
'http://www.kfc365.club',
'https://www.kfc365.club',
'http://6.chuhaivp.best',
'https://6.ccyy01.shop',
'https://6.chuhaivp.best',
'http://47.239.18.245',
'http://47.76.154.126',
'https://205.198.64.9',
'http://www.kuaileigo.cc',
'http://www.kuaileixingxi.cc',
'https://kuaileihuiyuan.cc',
'http://api.shanhai.one',
'https://154.212.135.207',
'https://47.76.154.126',
'https://6.qiang666.best',
'http://6.qiang666.shop',
'http://wolun001.chaosu202501.com',
'http://wolun003.chaosu202501.com',
'https://wolun001.chaosu202501.com',
'https://172.247.189.150',
'https://45.77.248.18',
'http://205.198.64.196',
'http://154.26.238.208',
'https://www.vcnetapp.top',
'https://www.breakthewall.win',
'http://www.breakthewall.win',
'http://150.241.206.196:8001',
'https://162.0.236.168',
'https://glgl.win',
'http://52.184.68.138',
'http://6.qiang666.best',
'https://www.vc-netapp.top',
'http://www.vc-netapp.top',
'https://52.163.94.66',
'https://6.qiang666.shop',
'https://abc-66.17788.xyz',
'http://20.2.193.91',
'http://205.198.64.9',
'http://link01.shanhai.me',
'http://link06.shanhai.me',
'https://link02.shanhai.one',
'https://link02.shanhai.me',
'http://link01.shanhai.one',
'http://link02.shanhai.one',
'http://link03.shanhai.one',
'https://link07.shanhai.me',
'https://link05.shanhai.one',
'https://link01.shanhai.me',
'http://link07.shanhai.me',
'https://link08.shanhai.me',
'http://link06.shanhai.one',
'https://link07.shanhai.one',
'http://link05.shanhai.me',
'https://link05.shanhai.me',
'https://link03.shanhai.one',
'http://link08.shanhai.me',
'https://link10.shanhai.me',
'https://link03.shanhai.me',
'https://link08.shanhai.one',
'http://link10.shanhai.one',
'http://link10.shanhai.me',
'http://link09.shanhai.one',
'https://link09.shanhai.one',
'https://link06.shanhai.me',
'http://link08.shanhai.one',
'https://link09.shanhai.me',
'http://link05.shanhai.one',
'https://link01.shanhai.one',
'http://link02.shanhai.me',
'http://link04.shanhai.one',
'https://link04.shanhai.me',
'https://link10.shanhai.one',
'https://7web.lol',
'https://66.qiang666.best',
'http://66.qiang666.shop',
'https://156.251.189.229',
'http://wuxianjc.top',
'http://170.205.30.75',
'https://117.18.13.72',
'https://20.2.165.145',
'https://52.184.68.138',
'https://185.254.97.16',
'https://152.67.7.167',
'https://20.2.193.91',
'http://kuaileihuiyuan.cc',
'https://52.229.206.241',
'http://185.139.7.29',
'https://66.qiang666.shop',
'http://66.qiang666.best',
'https://47.239.158.185',
'https://205.198.64.196',
'https://wolun22202.chaosu202502.xyz',
'https://ce.wolun8.com',
'http://aaa.waiqite.com',
'http://wolun22201.chaosu202502.xyz',
'http://wolun33302.chaosu202503.xyz',
'http://107.181.239.10',
'http://wolun33301.chaosu202503.xyz',
'http://ce.wolun8.com',
'https://wolun33303.chaosu202503.xyz',
'http://wolun33303.chaosu202503.xyz',
'https://wolun33302.chaosu202503.xyz',
'http://52.184.68.62',
'http://wolun002.chaosu202501.com',
'http://183.128.136.155:55555',
'http://117.18.13.72',
'http://45.77.248.18',
'http://wolun22203.chaosu202502.xyz',
'http://c.aaammmggg.com',
'https://aaa.waiqite.com',
'https://wolun22201.chaosu202502.xyz',
'https://wolun22203.chaosu202502.xyz',
'https://cc04.aaaspeed.pro',
'http://wolun22202.chaosu202502.xyz',
'https://47.238.152.119',
'http://dxdx.life',
'http://74.48.66.237',
'http://20.2.165.145',
'http://52.229.206.241',
'https://dxdx.life',
'http://splla1ecx46ae0t.life',
'http://hssl8088.icu',
'https://www.aaammmggg.com',
'https://wolun33301.chaosu202503.xyz',
'https://splla1ecx46ae0t.life',
'https://185.139.7.29',
'http://111.230.28.249',
'https://app.ladder-cat.cc',
'http://app.ladder-cat.cc',
'http://app.tizimao.xyz',
'https://app.tizimao.xyz',
'https://www.kuailei6.cc',
'http://www.kuaileixingxi.top',
'https://www.kuaileixingxi.top',
'http://www.kuailei6.cc',
'https://hash.pbnma.lol',
'https://adc1.fhcloud.xyz',
'http://adc2.fhcloud.xyz',
'https://fhcloud.icu',
'http://fhcloud.icu',
'https://fhcloud.gweuc.cn',
'http://hash.pbnma.lol',
'http://fhcloud.gweuc.cn',
'http://adc1.fhcloud.xyz',
'https://246cy.gravity001.top',
'http://246cy.gravity001.top',
'http://ufo.gravity001.top',
'https://ufo.gravity001.top',
'https://cs666.spacex2045net.icu',
'http://cs666.spacex2045net.icu',
'https://ncc.norton-cloud.com',
'http://ncc.norton-cloud.com',
'https://nc.xn--jvrq6s40z034a.xn--fiqs8s',
'http://nc.xn--jvrq6s40z034a.xn--fiqs8s',
'https://www.fhcloud.xyz',
'https://adc2.fhcloud.xyz',
'https://adc2.dylj.link',
'http://dy.dyyyy.top',
'https://win.douyun.us',
'http://win.douyun.us',
'https://douyunjiasu.sbs',
'http://service-a4rgovvz-202402.douyunyun.sbs',
'https://dy.dyyyy.top',
'https://douyunyun.sbs',
'https://service-a4rgovvz-202402.douyunyun.sbs',
'https://dyyyy.top',
'http://douyunjiasu.sbs',
'http://douyunyun.sbs',
'http://dyyyy.top',
'https://cdn.ssidcloud.com',
'http://cdn.ssidcloud.com',
'http://wwl.xn--jvrq6s40z034a.xn--fiqs8s',
'https://wwl.xn--jvrq6s40z034a.xn--fiqs8s',
'https://170.205.30.75',
'https://188.253.5.240',
'http://us.pbnma.lol',
'https://us.pbnma.lol',
'https://104.234.155.26',
'https://74.48.66.237',
'http://d2.chaosu888.com',
'https://d1.wolun6.com',
'https://d1.wolun7.com',
'https://d1.wolun999.com',
'http://d1.wolun444.com',
'http://d2.wolun6.com',
'http://d1.wolun7.com',
'https://d1.wolun555.com',
'http://d1.chaosu555.com',
'http://d2.wolun8.com',
'https://d2.chaosu777.com',
'http://d1.wolun999.com',
'http://d2.chaosu555.com',
'https://d2.chaosu888.com',
'http://d2.wolun999.com',
'https://d2.wolun6.com',
'http://d1.wolun555.com',
'https://d2.chaosu555.com',
'http://d1.wolun6.com',
'http://d1.chaosu888.com',
'https://d2.wolun8.com',
'https://d2.wolun999.com',
'https://d2.wolun7.com',
'https://d1.chaosu555.com',
'https://d1.wolun444.com',
'https://d1.chaosu888.com',
'http://d2.wolun7.com',
'http://d2.chaosu777.com',
'https://d2.wolun555.com',
'http://d2.wolun555.com',
'https://d1.wolun8.com',
'http://d1.wolun8.com',
'https://a.vcnet.sbs',
'https://b.vcnet.sbs',
'http://b.vcnet.sbs',
'https://www.vcnetapp.sbs',
'http://www.vcnetapp.sbs',
'https://b.vcnetapp.sbs',
'http://b.vcnetapp.sbs',
'https://a.vcnetapp.sbs',
'http://a.vcnetapp.sbs',
'https://www.vcnet.sbs',
'http://y50o1.123vvv456.one',
'https://y50o1.123vvv456.one',
'http://tk88.usero.cn',
'https://tk88.usero.cn',
'https://owlbam.com',
'https://52.184.68.62',
'http://a.112664.xyz',
'https://80.85.247.129',
'http://a.977344.xyz',
'https://www.joeshop.shop',
'http://www.joeshop.shop',
'https://joeshop.shop',
'http://joeshop.shop',
'https://166.88.55.45',
'http://a.355644.xyz',
'https://app01.i99.uk',
'http://app01.i99.uk',
'http://vip.77com.com',
'https://tkzc88.usero.cn',
'http://tkzc88.usero.cn',
'https://tzm.i99.uk',
'http://tzm.i99.uk',
'https://touanyun99.usero.cn',
'http://touanyun99.usero.cn',
'http://laddercat-dns.i99.uk',
'https://laddercat-dns.i99.uk',
'https://vip.77com.com',
'https://ssid.dggs.org',
'http://ssid.dggs.org',
'http://47.83.153.126:6622',
'https://888.7788.gg',
'http://888.7788.gg',
'https://bcc.touanyun.shop',
'https://www.touan.shop',
'http://www.touan.cc',
'http://www.touan.xyz',
'https://touanyun.shop',
'http://touanyun.shop',
'http://acc.touanyun.shop',
'http://bcc.touanyun.shop',
'https://acc.touanyun.shop',
'http://www.touan.shop',
'https://www.touan.xyz',
'http://9.touan.xyz',
'http://9.touan.shop',
'http://9.touan.cc',
'https://9.touan.xyz',
'https://www.touan.cc',
'https://9.touan.shop',
'https://9.touan.cc',
'http://52.163.62.85',
'http://172.105.237.100',
'http://115.196.175.233:55555',
'https://8.tiankong.shop',
'http://huoshaoyun.pro',
'http://app.mayun01.pro',
'https://app.mayun01.pro',
'http://141.148.180.168:7003',
'http://123xxx456.top',
'http://cdn.wjyhatat.monster',
'http://wjyhalou.makeup',
'https://cdn.wjyhatat.monster',
'http://175.178.42.155',
'http://wjyhatat.monster',
'http://tzm.tz8.uk',
'https://tzm.tz8.uk',
'https://lmy.world',
'http://lmy.world',
'https://zcc.qiang666.best',
'http://v2.dmyeyedm.com',
'https://v2.dmyeyedm.com',
'https://sub9832-health.fengchiyx.xyz',
'https://gameinfo.wiki',
'https://acc.qiang666.best',
'https://daxun.me',
'https://deyoufcvip.icu',
'http://deyoufcvip.icu',
'https://104.234.155.134',
'https://212.34.129.24',
'https://45.32.11.125',
'http://cdn1.ssidcloud.com',
'http://cdn2.ssidcloud.com',
'https://cdn1.ssidcloud.com',
'https://cdn2.ssidcloud.com',
'https://dash.coneapp.top',
'http://65.75.209.206:2223',
'https://107.172.144.72',
'https://45.145.72.122',
'http://www.daxun.me',
'https://www.daxun.me',
'https://api.douyun.us',
'http://api.douyun.us',
'https://47.76.177.174',
'https://4t4.icu',
'http://4c4.xyz',
'https://4c4.xyz',
'https://188.253.5.245',
'http://122.233.226.41:55555',
'https://20.2.155.198',
'http://205.198.64.112',
'http://kao.1880671.xyz:55555',
'https://141.147.161.152',
'http://1a2c.123yes456.rest',
'https://23.230.108.212',
'https://1a2c.123yes456.rest',
'https://172.247.44.25',
'https://107.173.85.15',
'http://www.m78starcloud.com',
'https://www.m78starcloud.com',
'http://52.184.65.57',
'https://shanhai.me',
'https://api.shanhai.one',
'http://www.kukudogs.com',
'https://www.kukudogs.com',
'http://999.touan.shop',
'https://999.touan.cc',
'http://999.touan.cc',
'http://999.touan.xyz',
'https://999.touan.shop',
'https://999.touan.xyz',
'http://183.156.208.201:55555',
'http://sub1.fhcloud.click',
'https://sub2.fhcloud.click',
'http://sub2.fhcloud.click',
'https://sub1.fhcloud.click',
'https://666.8877.gg',
'http://tanjiecn.buzz',
'https://tanjiecn2.buzz',
'http://tanjie1.buzz',
'http://tanjiecn2.buzz',
'https://tanjiecn.buzz',
'https://tanjie1.buzz',
'https://xyl.123kpl456.top',
'http://xyl.123kpl456.top',
'https://45.136.15.182',
'http://zcc.fxjs.best',
'https://zcc.qejs.best',
'http://bcc.fxjh.shop',
'http://bcc.fxjs.best',
'https://bcc.qejs.best',
'https://qejs.best',
'https://acc.fxjs.best',
'http://nnn.touan.cc',
'http://acc.fxjh.shop',
'https://zcc.fxjs.best',
'https://bcc.fxjh.shop',
'https://fxjh.shop',
'http://acc.fxjs.best',
'https://zcc.fxjh.shop',
'https://bcc.fxjs.best',
'https://acc.fxjh.shop',
'https://nnn.touan.cc',
'https://fxjs.best',
'http://qejs.best',
'http://acc.qejs.best',
'https://zxc.touan.cc',
'http://zxc.touan.cc',
'https://acc.qejs.best',
'http://fuck996.icu',
'https://fuck996.icu',
'https://chaosu555.com',
'https://52.184.65.57',
'https://link06.shanhai.one',
'http://link07.shanhai.one',
'https://103.134.144.226',
'https://52.175.20.77',
'http://link09.shanhai.me',
'http://link03.shanhai.me',
'http://link04.shanhai.me',
'https://link04.shanhai.one',
'http://sscy.cc',
'https://www.sscy.cc',
'http://www.sscy.cc',
'https://sscy.cc',
'https://qiang666.shop',
'https://chuhaivp.best',
'http://chuhaivp.best',
'https://qiang666.best',
'http://qiang666.best',
'https://huoshaoyun.pro',
'https://cn1.huoshaoyun.pro',
'http://52.175.20.77',
'http://192.3.134.164',
'https://ccc.abcd1234.shop',
'http://205.198.65.85:10010',
'http://36.22.243.236:55555',
'https://wcc.qie.sa.com',
'http://tkzc.shop',
'https://www.qie.sa.com',
'https://qie.sa.com',
'https://154.26.238.208',
'https://ccc.chaosu777.com',
'http://ccc.chaosu777.com',
'http://xn--8y0a963a.vip',
'https://xn--8y0a963a.vip',
'https://api.www77com.com',
'https://a.dzbnas.top',
'https://b.dzbnas.top',
'http://8.212.14.205',
'https://pkhub.net',
'http://pkhub.net',
'http://47.57.180.238',
'https://38.6.199.111',
'http://122.231.67.179:55555',
'https://fan.jisudashi.xyz',
'http://fan.jisudashi.xyz',
'http://kukudogapi.ggame.one',
'http://cxapi.ggame.cyou',
'https://cxapi.ggame.cyou',
'https://kukudogapi.ggame.one',
'http://glgl.win',
'https://pay.tz8.uk',
'http://pay.tz8.uk',
'https://yeszl.top',
'http://yeszl.top',
'http://deyoufcvip.yeszl.top',
'https://deyoufcvip.yeszl.top',
'https://dn1e-u8.868158.xyz',
'http://dn1e-u8.868158.xyz',
'https://jisu.ijdt.cn',
'https://conev1.top',
'https://touan.cc',
'http://touan.cc',
'http://38.55.199.174',
'http://60.176.32.98:55555',
'http://194.233.95.235:10001',
'http://zz.lmy.world',
'https://zz.lmy.world',
'https://bmw.safeboard.top',
'http://bmw.safeboard.top',
'https://a.douyun.sbs',
'http://b.douyun.sbs',
'http://a.douyun.sbs',
'http://1yesl1lli.123yes456.rest',
'https://1yesl1lli.123yes456.rest',
'https://douyun.sbs',
'https://www.douyun.sbs',
'http://www.douyun.sbs',
'https://b.douyun.sbs',
'http://douyun.sbs',
'https://bcc.chuhaivp.best',
'http://zcc.ccyy01.shop',
'http://acc.chuhaivp.best',
'http://acc.ccyy01.shop',
'http://zcc.qiang666.shop',
'http://acc.abcd1234.shop',
'http://zcc.qiang666.best',
'http://acc.qiang666.best',
'http://bcc.qiang666.best',
'http://bcc.chuhaivp.best',
'http://ccc.abcd1234.shop',
'http://acc.qiang666.shop',
'https://bcc.ccyy01.shop',
'http://zcc.chuhaivp.best',
'https://bcc.qiang666.shop',
'http://bcc.ccyy01.shop',
'https://zcc.ccyy01.shop',
'https://zcc.qiang666.shop',
'https://acc.chuhaivp.best',
'https://acc.ccyy01.shop',
'https://zcc.chuhaivp.best',
'https://acc.qiang666.shop',
'https://bcc.qiang666.best',
'https://proxigo.pro',
'https://qieyun.best',
'https://zcc.tiankong.shop',
'http://zcc.tiankong.shop',
'http://qieyun.best',
'https://ccc.tiankong.shop',
'http://zcc.tiankong.best',
'https://ccc.tiankong.best',
'http://ccc.tiankong.best',
'http://ccc.tiankong.shop',
'https://20.2.113.190',
'http://conev2.top',
'https://cloudvpnadmin.ddos.sale',
'http://b.vc-net.cfd',
'http://cloudvpnadmin.ddos.sale',
'https://b.vcnetapp.top',
'https://a.xiaoooo.online',
'https://xiaoooo.online',
'http://a.xiaoooo.online',
'http://www.vc-net.cfd',
'http://a.vc-net.cfd',
'https://a.vc-net.cfd',
'https://b.vc-net.cfd',
'https://a.vcnetapp.top',
'https://ccc.laohu.best',
'https://acc.gugeyun.best',
'https://acc.laohu.best',
'http://acc.laohu.best',
'https://bcc.gugeyun.best',
'http://www.kuaile3.com',
'http://xiaoooo.online',
'https://38.47.204.52',
'http://38.6.226.196',
'https://154.23.181.74',
'http://205.198.65.85',
'https://www.qcyun.us',
'http://iata.anying.cc',
'http://www.2adsf.xyz',
'https://www.2adsf.xyz',
'https://154.83.84.99',
'https://158.178.240.113',
'https://205.198.65.85',
'http://bcc.laohu.best',
'https://ccc.gugeyun.best',
'https://bcc.laohu.best',
'http://bcc.gugeyun.best',
'http://ccc.laohu.best',
'https://www.kuaile3.com',
'http://38.6.226.196:8001',
'https://dingyue.ijdt.cn',
'http://api.www77com.com',
'https://117.18.13.197',
'http://156.243.244.95:52020',
'http://38.47.103.74:52020',
'https://c.wolun555.com',
'http://cf1.cnsing.top',
'http://cf1khd.cnsing.top',
'https://cf1khd.cnsing.top',
'https://cf1.cnsing.top',
'http://dingyue.ijdt.cn',
'https://185.172.39.18',
'http://jisudashi.ijdt.cn',
'http://stneo.web1234.life',
'https://thesyeec7l60ouav1lz0tesk.top',
'https://iata.anying.cc',
'https://stneo.web1234.life',
'https://jisudashi.ijdt.cn',
'http://jisu.ijdt.cn',
'https://aaa.chaosu777.com',
'http://aaa.chaosu666.com',
'http://bbb.chaosu666.com',
'http://ccc.chaosu222.com',
'https://aaa.chaosu666.com',
'https://aaa.chaosu555.com',
'https://ccc.chaosu666.com',
'http://m.chaosu111.com',
'https://ccc.chaosu222.com',
'http://c.chaosu333.com',
'http://ccc.chaosu666.com',
'https://iata.xnnow.com',
'http://iata.xnnow.com',
'http://7web.lol',
'https://7.web1234.life',
'https://nc.norton-cloud.com',
'http://20.2.152.198',
'http://20.2.113.190',
'http://194.233.95.235',
'http://1880671.xyz',
'https://1880671.xyz',
'https://20.2.152.198',
'https://38.6.226.251',
'http://deyoufcvip.top',
'http://115.205.249.205:55555',
'http://125.118.189.101:55555',
'http://shanhai.one',
'https://deyoufcvip.top',
'http://d2.chaosu333.com',
'https://d1.chaosu666.com',
'http://d2.chaosu666.com',
'https://d1.chaosu444.com',
'https://d1.chaosu222.com',
'https://d1.chaosu777.com',
'http://d1.chaosu777.com',
'https://d2.chaosu666.com',
'https://d2.chaosu333.com',
'http://d2.chaosu222.com',
'https://d2.wolun444.com',
'https://d2.chaosu222.com',
'http://d1.chaosu666.com',
'http://d1.chaosu222.com',
'http://d2.wolun444.com',
'http://d2.chaosu444.com',
'https://d2.chaosu444.com',
'http://d1.chaosu444.com',
'https://d1.chaosu333.com',
'http://d1.chaosu333.com',
'http://www.qinxin999.xyz',
'http://b.98kjc.cyou',
'https://www.qinxin999.xyz',
'https://qinxin999.xyz',
'https://a.98kjc.cyou',
'https://b.98kjc.cyou',
'http://a.98kjc.cyou',
'http://38.6.226.251',
'https://205.198.65.251',
'https://20.255.249.251',
'https://yun.tz8.uk',
'http://yun.tz8.uk',
'http://api.app.cyberguard.cfd',
'https://api.app.cyberguard.cfd',
'https://g875f00.cdn.cdn1234.top',
'http://g875f00.cdn.cdn1234.top',
'http://141.148.180.168:7001',
'https://47.242.23.164',
'http://app.appjackma.lol',
'https://app.appjackma.lol',
'http://dou.douapi.top',
'https://101.42.5.237',
'https://48.218.144.215',
'https://goney.direct.quickconnect.to',
'https://acc.abcd1234.shop',
'https://sub.sillygoose.icu',
'http://www.sillygoose.icu',
'http://sub.sillygoose.icu',
'https://sillygoose.icu',
'https://www.sillygoose.icu',
'http://sillygoose.icu',
'http://125.122.80.169:55555',
'http://154.40.33.218:54169',
'http://146.56.232.55:82',
'https://52.175.16.63',
'https://a.vc-netapp.top',
'http://wsdyltjkyvx.quwanl.xyz',
'https://wsdyltjkyvx.quwanl.xyz',
'http://wzippzzposw.quwanl.xyz',
'https://wzippzzposw.quwanl.xyz',
'http://wtcrfuocgjy.quwanl.xyz',
'https://wtcrfuocgjy.quwanl.xyz',
'http://wjyniuniu.sbs',
'http://www.98kjc.cyou',
'https://www.98kjc.cyou',
'https://socool.xiao-diao-si.club',
'http://socool.xiao-diao-si.club',
'http://1.iclashnode.com',
'https://1.iclashnode.com',
'https://spacex2045ce0l10oreynet.buzz',
'http://spacex2045ce0l10oreynet.buzz',
'http://cs.spacex2045ce0l10oreynet.buzz',
'https://cs.spacex2045ce0l10oreynet.buzz',
'https://api3.luck855.com',
'https://api1.luck855.com',
'https://104.46.212.134',
'https://dingyue.life',
'http://www.dingyue.life',
'http://www.qiang666.best',
'https://www.qiang666.best',
'http://zxc.qiang666.shop',
'http://nnn.qiang666.shop',
'https://nnn.qiang666.shop',
'https://zxc.qiang666.shop',
'https://www.qiang666.shop',
'http://www.qiang666.shop',
'https://nnn.qiang666.best',
'http://nnn.qiang666.best',
'https://www.dingyue.life',

'https://billing.qlkxsw.com',
'http://billing.qlkxsw.com',
'http://billing.qlkxsw.net',
'https://billing.qlkxsw.net',

'https://billing.qlkxsw.org',
'http://billing.qlkxsw.org',
'http://b.98kjc.com',
'https://b.98kjc.com',
'http://a.98kjc.com',
'https://cdn33.wjyhalou.makeup',
'https://m35.wjyhalou.makeup',
'https://cdn03.wjyhalou.makeup',
'https://qf33.wjyhalou.makeup',
'https://cdn25.wjyhalou.makeup',
'https://qd57.wjyhalou.makeup',
'https://cc001.xyz',
'https://48.218.149.0',
'https://douyun.pro',
'http://douyun.pro',
'http://nuonuonet.uk',
'https://nuonuonet.uk',
'https://sub.fq5201314.uk',
'https://vpslamps.uk',
'http://sub.fq5201314.uk',
'http://vpslamps.uk',
'http://555.dashi666vip.top',
'https://555.dashi666vip.top',

'https://khd2.vwo50.buzz',
'https://khd1.vwo50.buzz',
'https://khd3.vwo50.buzz',
'http://khd3.vwo50.buzz',
'http://khd2.vwo50.buzz',
'http://khd1.vwo50.buzz',
'http://ccc.touan.shop',
'https://acc.touan.shop',
'http://bcc.touan.shop',
'http://acc.touan.shop',
'https://ccc.touan.shop',
'https://bcc.touan.shop',
'http://52.187.147.72',
'https://www.douyun.biz',
'http://www.douyun.biz',
'http://45.138.69.17',
'http://48.218.144.215',
'https://www.98kjc.com',
'http://www.98kjc.com',

'http://b.douyun.biz',
'https://b.douyun.biz',
'http://a.douyun.biz',
'http://qinxin66.best',
'https://a.douyun.biz',
'https://qinxin66.best',

'https://www.vcnets.top',
'http://www.vcnets.top',


'https://www.luck855.com',

'https://www.jisudashida.shop',
'http://www.jisudashida.shop',
'https://154.23.181.95',
'https://qinxin888.shop',
'http://qinxin888.shop',
'http://qinxin999.xyz',
'http://ccc.fxjh.shop',
'http://kfc365.club',
'https://aaabbbckc.xyz',
'https://kfc365.club',
'https://1a2b3c4d.xyz',
'http://cc-11.top',
'https://205.198.66.103',
'http://nfsih46.vcnet.cfd',
'http://rtxig51.vcnet.cfd',
'http://dalin.vcnet.cfd',
'http://8.vcnet.cfd',
'http://bjejx4.vcnet.cfd',
'http://97.vcnet.cfd',
'https://8.vcnet.cfd',
'http://75.vcnet.cfd',
'https://rtxig51.vcnet.cfd',
'https://97.vcnet.cfd',
'https://5.vcnet.cfd',
'https://dalin.vcnet.cfd',
'https://nfsih46.vcnet.cfd',
'http://46.vcnet.cfd',
'http://gqggt8.vcnet.cfd',
'https://bjejx4.vcnet.cfd',
'http://5.vcnet.cfd',
'https://75.vcnet.cfd',
'https://46.vcnet.cfd',
'https://gqggt8.vcnet.cfd',
'http://www.vcnet.cfd',
'https://www.vcnet.cfd',
'https://9.vcnet.cfd',
'http://9.vcnet.cfd',
'https://www.kuaileikeji.cc',
'http://www.kuaileikeji.cc',
'http://45.155.223.47',
'https://www.vc-net.cfd',
'https://16.vc-net.cfd',
'http://16.vc-net.cfd',
'https://ufo.zlyes.life',
'http://ufo.zlyes.life',
'http://104.168.88.145',
'https://touan.xyz',
'https://jack.123abc456.top',
'http://jack.123abc456.top',
'http://qieyunshop.com',
'https://qieyunshop.com',
'http://48.218.32.96',
'http://sub.dns-yun.com',
'http://sub.laddercat.uk',
'https://sub.dns-yun.com',
'https://142.171.81.82',
'http://aaa.chaosu555.com',
'https://bbb.chaosu666.com',
'https://c.wolun8.com',
'https://bbb.chaosu777.com',
'https://c.chaosu333.com',
'http://c.wolun8.com',
'https://aaa.chaosu333.com',
'http://aaa.chaosu333.com',
'https://web.stneo.help',
'http://web.stneo.help',
'https://7.web123.click',
'http://7.web123.click',
'https://45.155.223.47',
'http://48.210.80.10',
'http://47.238.139.252:8888',
'http://dy4.huaye.buzz',
'https://dy1.huaye.buzz',
'https://dy3.huaye.buzz',
'https://dy5.huaye.buzz',
'http://dy3.huaye.buzz',
'https://dy2.huaye.buzz',
'http://dy1.huaye.buzz',
'http://dy5.huaye.buzz',
'http://dy2.huaye.buzz',
'https://dy4.huaye.buzz',
'https://ccc.fxjh.shop',
'http://aak.lol',
'https://liulangid.eu.org',
'http://liulangid.eu.org',
'https://aak.lol',

'http://sslar.xyz',
'https://4.sslar.xyz',
'https://1.sslar.xyz',
'https://sslar.xyz',
'https://a.123tt.one',
'http://a.123tt.one',
'https://www.shizi666.top',

'http://web.tizimao.uk',
'https://web.tizimao.uk',
'https://sub.tizimao.uk',
'http://sub.tizimao.uk',

'https://def.zlyes.shop',
'https://123.zlyes.shop',
'https://dalin.vcnetapp.sbs',
'http://dalin.vcnetapp.sbs',
'https://www.zlyes.life',
'http://zlyes.shop',
'https://abc.zlyes.shop',
'http://www.zlyes.life',
'https://cos.zlyes.life',
'http://vip.zlyes.shop',
'http://def.zlyes.shop',
'https://zlyes.shop',
'https://www.zlyes.shop',
'https://zlyes.life',
'http://zlyes.life',
'https://vip.zlyes.shop',
'http://abc.zlyes.shop',
'https://100.zlyes.life',
'http://100.zlyes.life',
'http://www.zlyes.shop',
'http://123.zlyes.shop',
'http://cos.zlyes.life',
'https://tizimao.uk',
'https://dns.laddercat.net',
'http://103.255.209.237:83',
'https://45.58.184.220',
'https://104.208.73.5',
'http://103.255.209.237:81',
'http://103.255.209.237:82',
'https://20.24.90.35',
'http://c33.abcjiasu.mom',
'https://c33.abcjiasu.mom',
'https://c22.abcjiasu.mom',
'http://c22.abcjiasu.mom',
'http://hhh.cc001.xyz',
'https://hhh.cc001.xyz',
'http://c11.abcjiasu.mom',
'http://www.cc001.xyz',
'https://www.cc001.xyz',
'https://kkk.cc001.xyz',
'http://kkk.cc001.xyz',
'https://c11.abcjiasu.mom',
'https://38.150.0.113',
'https://manage.csyun.xyz',
'http://manage.csyun.xyz',
'http://csyun1.t1csyun.shop',
'https://csyun1.t1csyun.shop',
'http://www.csyun.xyz',
'http://csyun.t1csyun.shop',
'https://csyun2.t1csyun.shop',
'http://csyun2.t1csyun.shop',
'https://www.csyun.xyz',
'https://csyun.t1csyun.shop',
'http://103.255.209.237',
'http://www3.mxyqjsq.cc',
'https://www3.mxyqjsq.cc',
'https://103.255.209.237',
'https://www.zcjd.one',
'http://20.205.63.163',
'http://20.205.62.240',
'http://sss.ruyawwj.com',
'https://sss.ruyawwj.com',
'https://nuonuoweb.uk',
'http://nuonuoweb.uk',
'https://123x6y9z.d01olikp.thesyeec7l60ouav1lz0tesk.top',
'http://123x6y9z.d01olikp.thesyeec7l60ouav1lz0tesk.top',
'https://abc123xyz.thesyeec7l60ouav1lz0tesk.top',
'http://abc123xyz.thesyeec7l60ouav1lz0tesk.top',
'https://jisudashi.ianong.cn',
'http://jisudashi.ianong.cn',
'http://23.224.55.23:20001',
'https://www.sillygoose.cloud',
'https://api.sillygoose.cloud',
'http://dy.sillygoose.cloud',
'http://api.sillygoose.cloud',
'https://dy.sillygoose.cloud',
'https://45.134.9.170',
'https://38.47.205.28',
'https://cow.vc-netapp.top',
'http://cow.vc-netapp.top',
'https://20.205.62.240',
'https://20.24.225.68',
'https://107.151.240.106',
'https://azhuang.shop',
'http://azhuang.shop',
'https://65.75.209.228',
'https://zcc.qiangshi.xyz',
'http://qiangshi.xyz',
'https://qiangshi.xyz',
'https://v2b.529808.xyz',
'http://v2b.529808.xyz',
'http://157.245.200.182:8001',
'http://www.shizi666.top',
'http://alytx.cf',
'https://alytx.cf',
'https://154.40.46.22',
'https://20.205.63.163',
'http://104.208.73.5',
'http://www.800water.xyz',
'http://www.800mlc.com',
'https://www.800water.xyz',
'https://www.800mlc.com',
'https://ccc.xinqin2233.xyz',
'http://main.whysless.com',
'https://main.whysless.com',
'http://vcc.qinxin5566.top',
'https://vcc.qinxin5566.top',
'https://154.44.30.235',
'http://23.224.55.23:20002',
'https://dmo2.sudu.date',
'http://dmo2.sudu.date',
'https://www.mayi.pro',
'http://zhu.shijisu.com',
'https://zhu.shijisu.com',
'https://ccc.tkzc.shop',
'https://bcc.tkzc.shop',
'http://bcc.tkzc.shop',
'http://ccc.tkzc.shop',
'https://acc.tkzc.shop',
'http://acc.tkzc.shop',
'http://dog.vc-netapp.top',
'https://dog.vc-netapp.top',
'http://tizimao.cc',
'https://48.218.144.132',
'http://65.75.209.228:2096',
'http://qinxin5566.top',
'https://qinxin5566.top',
'https://141.11.132.164',
'http://20.24.225.68',
'https://141.11.174.204',
'http://one.vcnet.sbs',
'https://one.vcnet.sbs',
'https://cy.vc-netapp.top',
'https://v1.jdy02.xyz',
'http://jdy02.xyz',
'https://jdy02.xyz',
'http://v1.jdy02.xyz',
'http://jdy03.xyz',
'https://jdy03.xyz',
'https://ivpn3.cc',
'https://www.ivpn3.cc',
'https://www.ivpn2.cc',
'http://www.ivpn3.cc',
'https://ivpn2.cc',
'http://www.ivpn1.cc',
'http://ivpn1.cc',
'http://www.ivpn2.cc',
'https://ivpn1.cc',
'http://ivpn2.cc',
'http://ivpn3.cc',
'https://www.ivpn1.cc',
'http://139.180.202.178',
'https://146.190.50.231',
'http://cloudcat.top',
'https://cloudcat.top',
'https://104.208.79.42',
'http://csyun.xyz',
'https://csyun.xyz',
'http://subscribe.csyun.xyz',
'https://mine.csyun.xyz',
'https://subscribe.csyun.xyz',
'http://mine.csyun.xyz',
'https://nccc.rc25.cn',
'http://nccc.rc25.cn',
'https://107.148.239.242',
'http://65.75.209.228',
'https://cc2.cc001.xyz',
'http://www.dd136.top',
'https://www.dd136.top',
'https://www.slplus.one',
'http://wiki1.dd136.top',
'https://wiki1.dd136.top',
'http://iplc.lat',
'http://mgjs.pw',
'http://touantrade.shop',
'https://20.205.121.232',
'https://64.64.239.182',
'https://77.221.149.194',
'https://180.131.144.233',
'https://ccc.touan.xyz',
'https://bcc.touan.xyz',
'http://bcc.touan.xyz',
'http://acc.touan.xyz',
'https://acc.touan.xyz',
'http://ccc.touan.xyz',
'http://dcc.touan.shop',
'https://dcc.touan.shop',
'https://104.194.78.222',
'http://v2s.one',
'https://v2s.one',
'https://20.243.120.12',
'https://20.24.81.111',
'http://20.24.81.111',
'http://console.qlvpn.com',
'http://one-kg.top',
'http://boluo123.top',
'https://one-kg.top',
'https://www.boluo123.top',
'https://boluo123.top',
'https://154.12.56.150',
'http://www.sillygoose.cloud',
'http://111.92.242.144:8001',
'http://104.208.79.42',
'http://www.ggame.cyou',
'https://www.ggame.cyou',
'http://kukudog.cyou',
'https://kukudog.cyou',
'http://www.kukudog.cyou',
'https://www.kukudog.cyou',
'http://azxc.chituma.buzz',
'https://azxc.chituma.buzz',
'https://ss.ggame.cyou',
'http://ss.ggame.cyou',
'https://195.201.167.12',
'https://20.247.4.128',
'http://64.64.239.182',
'http://157.245.200.182:7001',
'https://111.92.242.144',
'http://4.sslar.xyz',
'http://5.sslar.xyz',
'http://3.sslar.xyz',
'https://5.sslar.xyz',
'https://3.sslar.xyz',
'http://20.243.120.12',
'http://www.shenlan.lol',
'https://www.shenlan.lol',
'https://45.145.74.187',
'http://www.kuailei6.xyz',
'http://www.kuaile33.xyz',
'https://www.kuailei6.top',
'https://www.kuailei6.xyz',
'https://pub-1.api.hongancould.top',
'https://honganjsq.top',
'http://pub-1.api.hongancould.top',
'http://honganjsq.top',
'https://laoy.158258.xyz',
'https://123xxx456.filegear-sg.me',
'https://yes.123www456.top',
'http://yes.123www456.top',
'https://app01.shanhai.me',
'http://app01.shanhai.me',
'http://kfccloud.top',
'https://kfccloud.top',
'https://198.44.166.230',
'https://64.176.49.25',
'http://acc.tiankong.shop',
'http://bcc.skyshops.net',
'http://ccc.skyshops.net',
'http://bcc.tiankong.shop',
'https://bcc.tiankong.best',
'https://acc.tiankong.best',
'http://acc.skyshops.net',
'http://acc.tiankong.best',
'http://bcc.tiankong.best',
'https://bcc.skyshops.net',
'https://bcc.tiankong.shop',
'https://ccc.skyshops.net',
'https://acc.skyshops.net',
'https://acc.tiankong.shop',
'http://api.shanhai.me',
'https://api.shanhai.me',
'http://b.okxapp.org',
'https://103.41.7.50',
'http://20.205.121.232',
'http://console.sillygoose.cloud',
'https://console.sillygoose.cloud',
'https://sillygoose.cloud',
'http://jdy01.xyz',
'https://jdy01.xyz',
'https://8.210.115.244',
'https://yzc.ruyawwj.com',
'http://yzc.ruyawwj.com',
'https://jump2023.v2s.one',
'http://jump2023.v2s.one',
'https://yes5.xn--mesv7f5toqlp.com',
'http://www.lhy666666.buzz',
'https://www.lhy666666.buzz',
'https://www.lhy88888.xyz',
'http://www.lhy88888.cyou',
'http://www.lhy88888.xyz',
'https://www.lhy88888.cyou',
'http://lhy88888.xyz',
'http://lhy88888.cyou',
'http://www.slplus.one',
'https://lhy88888.cyou',
'https://lhy88888.xyz',
'https://lhy666666.buzz',
'http://20.247.96.40',
'http://c.xhj288.org',
'https://a.xhj288.org',
'http://a.xhj288.org',
'http://xhj288.org',
'https://b.xhj288.org',
'https://c.xhj288.org',
'http://b.xhj288.org',
'https://bt.xhj288.org',
'http://bt.xhj288.org',
'https://20.247.96.40',
'https://202.182.108.39',
'http://1.sslar.xyz',
'https://5.255.123.218',
'http://107.21.33.149',
'http://www.shenlan.one',
'https://www.shenlan.one',
'https://119.28.235.224',
'http://20.247.4.128',
'https://156.238.236.91',
'https://192.166.82.130',
'https://1.dd136.top',
'http://1.dd136.top',
'http://38.59.228.159',
'https://38.59.228.159',
'https://test.zcjd.one',
'http://test.zcjd.one',
'https://bt.deyoufc.com',
'http://bt.deyoufc.com',
'http://deyoufc.com',
'https://deyoufc.com',
'https://douyun.douyun.pro',
'http://douyun.douyun.pro',
'http://cat.vc-netapp.top',
'http://test.dd136.top',
'https://cat.vc-netapp.top',
'http://100.123www456.top',
'http://api.kfccloud.top',
'https://api.kfccloud.top',
'https://kkkk.kfccloud.top',
'http://kkkk.kfccloud.top',
'http://c.ajefficiency.com',
'https://149.62.47.148',
'http://47.76.94.210',
'http://test0.jiasuj.com',
'https://test0.jiasuj.com',
'https://141.11.132.116',
'https://b.okxapp.org',
'https://47.76.94.210',
'https://154.12.50.244',
'http://www.shenlan.lol',
'http://shenlan.lol',
'https://shenlan.lol',
'https://www.shenlan.lol',
'https://c.aaammmggg.com',
'https://www.chituma.top',
'http://www.chituma.top',
'https://43.134.56.239',
'http://dyapi.ggame.cyou',
'http://ss.ggame.one',
'https://dyapi.ggame.cyou',
'http://hdapi.ggame.cyou',
'https://ss.ggame.one',
'https://hdapi.ggame.cyou',
'https://116.206.92.98',
'http://1.czjiasu.com',
'https://198.44.166.196',
'https://1.czjiasu.com',
'https://[2604:9cc0:0:5cac::1]',
'http://103.152.221.200',
'https://101.33.218.231',
'https://30000.top',
'https://38.174.114.201',
'https://apopcloud.com',
'http://apopcloud.com',
'https://store.besnow.work',
'http://store.besnow.work',
'http://gos.wiki',
'https://gos.wiki',
'https://2.xigua.bar',
'https://1.xigua.bar',
'http://1.xigua.bar',
'http://2.xigua.bar',
'http://okk.tkzc.shop',
'https://ykk.tkzc.shop',
'https://ikk.tkzc.shop',
'https://tkk.tkzc.shop',
'http://ykk.tkzc.shop',
'http://ikk.tkzc.shop',
'http://ukk.tkzc.shop',
'https://okk.tkzc.shop',
'http://tkk.tkzc.shop',
'https://ukk.tkzc.shop',
'https://xiongmaojiasu.xyz',
'https://shizi666.icu',
'http://shizi666.icu',
'https://www.dashi666vip.buzz',
'http://www.dashi666vip.buzz',
'http://1.shejisudashi.top',
'https://1.shejisudashi.top',
'https://dashi666vip.buzz',
'http://dashi666vip.buzz',
'http://qcjiasu-9121-guanfang.qingcha.one',
'https://qcjiasu-9121-guanfang.qingcha.one',
'https://8.217.179.146',
'http://98k03.54188a.cyou',
'https://98k03.54188a.cyou',
'https://test666.kuaiyun.club',
'https://192.248.187.181',
'http://apap.surfx.one',
'https://apap.surfx.one',
'https://app.56vpn.cc',
'https://www.32000.app',
'http://www.56000.app',
'https://www.56000.app',
'http://v2.32000.app',
'http://sub.v2.39000.xyz',
'https://v2.32000.app',
'http://app.56vpn.cc',
'https://www.36000.app',
'https://sub.v2.39000.xyz',
'http://www.32000.app',
'http://www.36000.app',
'https://cl1.jiasuj.com',
'http://cl.jiasuj.com',
'https://cl.jiasuj.com',
'http://wujibian.com',
'https://www.wujibian.com',
'http://www.wujibian.com',
'https://95.214.165.63',
'http://192.248.187.181',
'https://89.213.0.88',
'https://38.174.114.200',
'http://1.touantrade.shop',
'https://1.touantrade.shop',
'http://74.48.44.148',
'https://107.172.216.177',
'http://130.162.159.78',
'https://sslar.top',
'http://www.sslar.top',
'https://www.sslar.top',
'https://mxyq01.xyz',
'https://130.162.159.78',
'https://38.174.114.202',
'http://dmo1.sudu.date',
'https://dmo1.sudu.date',
'https://64.23.234.17',
'https://172.105.217.56',
'https://45.79.236.123',
'https://172.104.60.85',
'https://170.64.184.163',
'http://45.79.236.123',
'http://172.235.26.7',
'http://170.64.184.163',
'http://shanhai.me',
'https://api-sub01.xmss.vip',
'https://api.xmss.vip',


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
