# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/3/25 14:57
# @FileName     :run_all.py
#IDE            :PyCharm
import unittest
from public.HTMLTestRunner import HTMLTestRunner
import time
if __name__ == "__main__":
    # 定义测试用例的存放路径
    test_dir = "./test_case/"
    discover = unittest.defaultTestLoader.discover(test_dir, "*.py")
    testReportDir = "./test_report/"
    nowTime = time.strftime("%Y-%m-%d%H%M%S", time.localtime())
    fileName = nowTime + ".html"
    # 定义测试路径和测试报告名字
    testReportDir_FileName = testReportDir + fileName
    fp = open(testReportDir_FileName, "wb")
    runner = HTMLTestRunner(stream=fp, title="自动化测试报告", description="用例执行情况")
    # 运行测试用例
    runner.run(discover)