import unittest
from public.get_excel import getExcel
from ddt import ddt,data
from public.test_request import getRequests
from public.log import logger
from config.project_config import base_url,get_token
import os
file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\test_file\\meiYe.xlsx'
excel=getExcel(file,'test_data')
test_data=excel.get_excel()
mylog=logger('unittest模块').get_logger()
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.token=get_token()
        #初始化测试数据
        self.test =excel.get_excel()
    @data(*test_data)
    def test_api(self,sub_data):
        mylog.info("执行第{0}条用例:{1}模块\n请求地址:{2}\n请求参数:{3}".format(sub_data['id'], sub_data['name'],base_url+sub_data['url'],sub_data['data']))
        http_data = getRequests(base_url + sub_data['url'], eval(sub_data['data'])).get_requests(sub_data['method']).json()
        try:
            # 断言，使用code进行断言
            self.assertEqual(sub_data['code'], http_data['status'])
            print("执行第{0}条用例:{1}模块\n请求地址:{2}\n请求参数:{3}".format(sub_data['id'], sub_data['name'],base_url+sub_data['url'],sub_data['data']))
            print("返回数据:{}".format(http_data))
            # 断言成功,设置测试结果
            test_result = 'Pass'
        except Exception as  e:
            print("执行第{0}条用例:{1}模块\n请求地址:{2}\n请求参数:{3}".format(sub_data['id'], sub_data['name'], base_url + sub_data['url'],sub_data['data']))
            print("返回数据:{}".format(http_data))
            mylog.info("执行接口测试错误:{}".format(e))
            # 断言不成功,设置测试结果
            test_result = 'Fail'
            raise e
        # 最后把测试结果,返回数据写到Excel表格
        finally:
            mylog.info("############开始写入测试结果############")
            excel.write_excel(sub_data['id'] + 1, 7, test_result)
            excel.write_excel(sub_data['id'] + 1, 8, str(http_data))
            mylog.info("############结束写入测试结果############")
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
