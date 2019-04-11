#!/usr/bin/env python3
# -*- coding : utf-8 -*-
import json

import time

import readExcel
from common.quest import ConfigHttp
import base64
from urllib import parse
import pymysql
import datetime

class demo:
    now = datetime.datetime.now()
    confighttp= ConfigHttp()
    confighttp.url ="http://track.hujiang.com/v4/track"
    confighttp.headers = {"Content-Type": "application/x-www-form-urlencoded",
                          "Cookie": "Qs_lvt_268254=1553837875; Qs_pv_268254=4028062231608616400; HJ_UID=571ef248-7a00-ab60-5d09-ccac1da58720; _REF=; _SREF_23=; _SREG_23=direct|; UM_distinctid=169c8192ebb1375-036c6a10b3bf7e-5d1f3b1c-1fa400-169c8192ebc613; Hm_lvt_aa6b628920225aa8723fe04b02129f18=1553840288; _SREF_20=; _SREG_20=direct|; _SREF_66=; _SREG_66=direct|; ClubAuth=39313936353430332e3062373663613164616236316532303063643131356334336564623232646334; hj_token=s_7b379929693734df23aae63ca9ffff84|NTdiNDdkYg==; _SREG_17=class.hujiang.com|; _SREF_17=https://class.hujiang.com/19394883/intro; _SREF_49=; _SREG_49=direct|; _SREF_9=http://2fa.sec.hujiang.com/?url%3Ddw.hujiang.com%252Fsetting%252F; _SREG_9=2fa.sec.hujiang.com|; TRACKSITEMAP=3%2C6%2C9%2C17%2C20%2C23%2C49%2C54%2C66%2C; _REG=direct|; HJ_SID=73dafbab-cad7-87cc-9eaa-36bf50b0fd09; HJ_CST=0; HJ_CSST_6=0; HJ_CSST_45=0; _SREG_6=ipo_jp_1_wzxmbitjkchid|ch_source%3Dipo_jp_1_wzxmbitjkchid; _SREF_45=https://www.hujiang.com/; HJ_SSID_6=95419e06-0288-40e1-ac2e-4fb93b1ad060; _SREF_6=https://www.hujiang.com/; HJ_SSID_45=95419e06-0288-40e1-ac2e-4fb93b1ad060; Qs_lvt_268254=1553837875; Qs_pv_268254=4028062231608616400; HJ_UID=571ef248-7a00-ab60-5d09-ccac1da58720; _REF=; _SREF_23=; _SREG_23=direct|; UM_distinctid=169c8192ebb1375-036c6a10b3bf7e-5d1f3b1c-1fa400-169c8192ebc613; Hm_lvt_aa6b628920225aa8723fe04b02129f18=1553840288; _SREF_20=; _SREG_20=direct|; _SREF_66=; _SREG_66=direct|; ClubAuth=39313936353430332e3062373663613164616236316532303063643131356334336564623232646334; hj_token=s_7b379929693734df23aae63ca9ffff84|NTdiNDdkYg==; _SREG_17=class.hujiang.com|; _SREF_17=https://class.hujiang.com/19394883/intro; _SREF_49=; _SREG_49=direct|; _SREF_9=http://2fa.sec.hujiang.com/?url%3Ddw.hujiang.com%252Fsetting%252F; _SREG_9=2fa.sec.hujiang.com|; TRACKSITEMAP=3%2C6%2C9%2C17%2C20%2C23%2C49%2C54%2C66%2C; _REG=direct|; HJ_SID=73dafbab-cad7-87cc-9eaa-36bf50b0fd09; HJ_CST=0; HJ_CSST_6=0; HJ_CSST_45=0; _SREG_6=ipo_jp_1_wzxmbitjkchid|ch_source%3Dipo_jp_1_wzxmbitjkchid; _SREF_45=https://www.hujiang.com/; HJ_SSID_6=95419e06-0288-40e1-ac2e-4fb93b1ad060; _SREF_6=https://www.hujiang.com/; HJ_SSID_45=95419e06-0288-40e1-ac2e-4fb93b1ad060; HJ_SSID_9=9100233c-9afe-b1d6-612b-6ea782307ffa; HJ_CSST_9=0"}
    oe = readExcel.OperateExcel("F:\dmpapi\data\虚拟子站.xlsx", "Sheet2")
    # 打开数据库连接

    db = pymysql.connect("192.168.36.92", "hadoop", "hujiang.123", "dw_utrack")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    start = 2
    end = oe.rows+1
    # end = 32

    i = start -1

    for row in range(start,end):
        url1 = str(oe.table.cell(row, 3).value)
        str2 = '{"hj_siteid":20,"hj_uid":"571ef248-7a00-ab60-5d09-ccac1da58720","hj_sid":"523710d6-3871-4f02-b471-aa4fea611f4e","hj_ssid":"e7453cca-2b7f-b288-cc19-cd908ff62a0c","hj_url":"' + url1 + '","hj_urlref":"","hjid":91965403,"hj_p":"{\\"res\\":\\"1920*1080\\",\\"wres\\":\\"1137*929\\",\\"bdhm\\":null,\\"title\\":\\"%E6%B2%AA%E6%B1%9F%E8%8B%B1%E8%AF%AD-%E6%B2%AA%E6%B1%9F%E6%97%97%E4%B8%8B%E8%8B%B1%E8%AF%AD%E5%AD%A6%E4%B9%A0%E8%B5%84%E8%AE%AF%E7%BD%91%E7%AB%99_%E5%85%8D%E8%B4%B9%E8%8B%B1%E8%AF%AD%E5%AD%A6%E4%B9%A0%E7%BD%91%E7%AB%99\\"}","hj_vt":0,"hj_sst":0,"hj_csst":0,"hj_st":0,"hj_cst":0,"hj_ref":"","hj_sref":"","hj_fp":344820995,"hj_v":"1.1.21","hj_ua":"mozilla/5.0 (windows nt 6.1; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/71.0.3578.98 safari/537.36","hj_t":1554865100955,"ch_source":"","hj_sr":"direct","hj_srp":"","hj_ssr":"direct","hj_ssrp":"","hj_tm":"pc","_":"ac8be5e98b48b997","is_sync":1}'
        str1 = parse.quote(str2)
        str1 = str1.replace("/", "%2F")
        str1 = str1.replace("%2A", "*")
        str1 = str1.replace("%28", "(")
        str1 = str1.replace("%29", ")")
        result = str(base64.b64encode(str1.encode()))
        result = result[2:-1]
        # print(result)
        i = i+1
        print(str1)
        print(str2)
        print(result)
        print("开始访问第"+str(i)+"行链接 : "+url1)
        confighttp.data = "d=" + result + "&t=1554185380840"
        # print(confighttp.data)
        confighttp.timeout = 15
        response = confighttp.post()
        # time.sleep(0.5)

    for j in range(10):
        time.sleep(1)
        print("sleep :",j,"seconds")
    confighttp.url = "http://utrack-api.qabi.hujiang.com/v2/dw/utrack/track_log"
    confighttp.headers = {"Content-Type": "application/json",
                          "Cookie": "Qs_lvt_268254=1553837875; Qs_pv_268254=4028062231608616400; HJ_UID=571ef248-7a00-ab60-5d09-ccac1da58720; _REF=; _SREF_23=; _SREG_23=direct|; UM_distinctid=169c8192ebb1375-036c6a10b3bf7e-5d1f3b1c-1fa400-169c8192ebc613; Hm_lvt_aa6b628920225aa8723fe04b02129f18=1553840288; _SREF_20=; _SREG_20=direct|; _SREF_66=; _SREG_66=direct|; _SREG_17=class.hujiang.com|; _SREF_17=https://class.hujiang.com/19394883/intro; _SREF_49=; _SREG_49=direct|; _SREF_9=http://2fa.sec.hujiang.com/?url%3Ddw.hujiang.com%252Fsetting%252F; _SREG_9=2fa.sec.hujiang.com|; TRACKSITEMAP=3%2C6%2C9%2C17%2C20%2C23%2C49%2C54%2C66%2C; _REG=direct|; _SREF_45=https://www.hujiang.com/; _SREG_6=www.hujiang.com|; hj_token=s_488d429141631f9be1063e3e9d6f4afd|NTdiNDdkYg==; ClubAuth=39313936353430332e3135383134663532343261653836333762323964623634666137633864393032; _SREF_6='https://www.hujiang.com/'"}


    i = start -1
    for row in range(start,end):
        # 使用 execute()  方法执行操作
        esrule = str(oe.table.cell(row, 1).value).replace("\\.","\\\\\.")
        # print(esrule)
        sql = "UPDATE dw_utrack.ut_web_rules SET es_url_rule='" + str(esrule) + "' WHERE id=156;"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("更新数据错误")
            oe.table.cell(row, 3).value = "更新数据错误"
            i = i+1
            continue
        data1 = {  "startTime": "2019-04-09 10:10:00","debug":"false","endTime": "2019-04-09 23:59:59",  "bHour": "13",  "bMinute": "10",  "eHour": "23",  "eMinute": "59",  "domain": "http://utrack-api.qabi.hujiang.com",  "domainId": "22",  "moduleId": "114", "visitId": "571ef248-7a00-ab60-5d09-ccac1da58720","pageSize": 200}
        confighttp.data = json.dumps(data1)
        confighttp.timeout = 15
        response = confighttp.post()
        print(response.text)
        lenth = len(str(json.loads(response.text)['data']["result"]))
        if lenth > 2:
            oe.set_value(row, 3,"pass")
        else:
            oe.set_value(row, 3, "failed")
        i = i + 1
        print("第"+str(i)+"行的上报结果为 : "+oe.table.cell(row, 3).value)
        # time.sleep(0.5)

    # 关闭数据库连接
    db.close()
    # 保存文件
    oe.save("F:\dmpapi\data\虚拟子站.xlsx")





