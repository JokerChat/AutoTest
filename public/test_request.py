# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/3/25 14:21
# @FileName     :test_request.py
#IDE            :PyCharm
import requests,json
from public.log import logger
from jsonpath import jsonpath
from public.get_excel import getExcel
import os
file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\test_file\\meiYe.xlsx'
excel=getExcel(file,'update')
mylog=logger('Requests模块').get_logger()
class getRequests:
    def __init__(self,url,data):
        self.url=url
        self.data=data
    def get_requests(self,method):
        try:
            if method=='get'or method=='GET':
                r=requests.get(self.url)
        except Exception as e:
            mylog.info("############get请求失败,原因:{}############".format(e))
        try:
            if method=='post' or method=='POST':
                r=requests.post(self.url,data=self.data)
                # if self.url.find('login')!=-1:
                #     token=jsonpath(r.json(),'$.data')[0]
                #     writeExcel=excel.write_excel(2,2,token)
                #     mylog.info("############写入token值成功############".format(token))
                mylog.info("############{}请求成功############".format(method))
                return  r
        except Exception as e:
            mylog.info("############post请求失败,原因:{}############".format(e))
if __name__=='__main__':
    url='http://meiye-gray-api.lvshou.me:7773/post/login'
    data={'username': '13119656020', 'password': 'lv123456'}
    re=getRequests(url,data).get_requests('POST')
    if url.find('login') != -1:
        token = jsonpath(re.json(), '$.data')[0]
        print(token)