# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/3/25 14:07
# @FileName     :project_config.py
#IDE            :PyCharm
import pymysql
import requests
from jsonpath import jsonpath
from public.get_excel import getExcel
import os
file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\test_file\\meiYe.xlsx'
excel=getExcel(file,'update')
#预发布数据库配置文件
gray_config={
        'host':'172.16.97.11',
        'port':3306,
        'user':'meidian',
        'password' : 'SdxPQo1w2K8=',
        'db': 'meidianyewu',
        'charset' :'utf8',
        'cursorclass':pymysql.cursors.DictCursor,
    }
#预发布接口地址
base_url='http://meiye-gray-api.lvshou.me:7773/'
def get_token():
        data = {'username': '13119656020', 'password': 'lv123456'}
        r1=requests.post(base_url+'post/login',data=data)
        payload = {'username': '18888888888', 'password': 'a123456'}
        r2=requests.post(base_url+'post/login',data=payload)
        token = jsonpath(r1.json(), '$.data')[0]
        sysToken=jsonpath(r2.json(), '$.data')[0]
        write_excel = excel.write_excel(2, 2, token)
        write_excel = excel.write_excel(3, 2, sysToken)
if __name__=='__main__':
        get_token()