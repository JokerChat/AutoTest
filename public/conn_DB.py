# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/3/25 14:47
# @FileName     :conn_DB.py
#IDE            :PyCharm
import pymysql
from config.project_config import gray_config
from public.log import logger
from public.get_excel import getExcel
import os
mylog=logger('Sql模块').get_logger()
class getDatabase(object):
    #初始化数据,读取配置文件
    def __init__(self):
        self.config=gray_config
        mylog.info("############初始化数据############")
    #连接数据库
    def connect(self):
        try:
            # 连接数据库
            self.conn=pymysql.connect(**self.config)
            mylog.info("############连接数据库成功############")
            #游标操作
            self.cursor = self.conn.cursor()
            mylog.info("############建立游标操作成功############")
        except Exception as e:
            mylog.info("############连接数据库失败:{}############".format(e))
    #关闭数据库
    def close(self):
        try:
            #关闭连接
            self.conn.close()
            mylog.info("############关闭连接成功############")
            #关闭游标操作
            self.cursor.close()
            mylog.info("############关闭游标成功############")
        except Exception as e:
            mylog.info("############关闭失败:{}############".format(e))
    #查询一条数据
    def get_one(self,sql,params=[]):
        try:
            result=None
            self.connect()
            mylog.info("############sql:{0}############".format(sql))
            self.cursor.execute(sql,params)
            result=self.cursor.fetchone()
            mylog.info("############查询单条数据成功############")
            self.close()
            return result
        except Exception as e:
            mylog.info("############查询失败:{}############".format(e))
    #查询sql所有数据
    def get_all(self,sql,params=[]):
        result=None
        self.connect()
        self.cursor.execute(sql,params)
        mylog.info("############sql:{0}############".format(sql))
        result=self.cursor.fetchall()
        mylog.info("############查询全部数据成功############")
        self.close()
        return result

    #插入数据操作，定义一个私有方法,只供内部class用
    def insert(self,sql,params=[]):
        mylog.info("############新增数据操作############")
        return self.__edit(sql,params)
    #修改数据操作
    def update(self,sql,params=[]):
        mylog.info("############修改数据操作############")
        return self.__edit(sql,params)
    #删除数据操作
    def delete(self,sql,params=[]):
        mylog.info("############删除数据操作############")
        return self.__edit(sql,params)
    #私有方法,传入sql,参数化
    def __edit(self,sql,params):
        result=0
        try:
            self.connect()
            result=self.cursor.execute(sql,params)
            mylog.info("############sql:{0}############".format(sql,params))
            self.conn.commit()
            mylog.info("############提交成功############")
            self.close()
            result=1
        except Exception as e:
            mylog.info("############提交失败:{}############".format(e))
        return result
if __name__=='__main__':
    pass