# coding=utf-8
import sys

"""在jenkins上配置环境变量和自定义变量后，仍可能返回找不到工程的包,需要导入工程地址，如下："""
sys.path.append("F://PycharmPyProject")
import unittest
import warnings
import ddt
import json
import time
from bcpinterface.handles.handle_ini import handle_ini
from bcpinterface.handles.handle_excel import handleExcel
from bcpinterface.handles.handle_logging import log
from bcpinterface.handles.header_script import get_header_value, write_header_value
from bcpinterface.handles.handle_relations import handleRelations
from bcpinterface.basePage.base_method import base_pages
from bcpinterface.handles.handle_result import write_result_value
from bcpinterface.handles.josn_script import jsonJudgment
from bcpinterface.handles.code_msg import CodeMsg
from bcpinterface.case.subject_files import submit_files


@ddt.ddt
class run_method(unittest.TestCase):

    def __init__(self, data):
        super().__init__()
        self.data = data

    def setUp(self):
        print("测试开始")
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        print("测试结束")

    @ddt.data(self.data)
    def test_run_main(self, rows_value):
        global header
        is_run = rows_value[3]
        i = handleExcel().relation_row_nums(rows_value[0])
        if is_run == 'yes':
            case_num = rows_value[0]
            itf_name = rows_value[1]
            log.info("接口名称：{}".format(itf_name))
            prerequisites = rows_value[2]
            method = rows_value[4]
            url = rows_value[5]
            relation_key = rows_value[12]
            data = rows_value[6]
            log.info('取出参数:{}'.format(data))
            log.info('取出参数类型:{}'.format(type(data)))
            is_header = rows_value[8]
            exp_result = rows_value[10]
            check_method = rows_value[13]
            base_url_key = rows_value[15]
            stop_time = rows_value[16]
            try:
                if is_header == 'yes':
                    """携带header"""
                    header = get_header_value(rows_value[14])
                """处理请求参数"""
                data = handleRelations.datas_return(method, prerequisites, data, relation_key)
                log.info('入参参数:{}'.format(data))
                log.info('入参参数类型:{}'.format(type(data)))
                if data == '{}' or data is None:
                    if prerequisites:
                        url = handleRelations.url_return(url, prerequisites)
                    else:
                        url = url
                """处理返回结果"""
                base_url = handle_ini.get_ini_value(base_url_key)
                if 'http' in url:
                    url = url
                else:
                    url = base_url + url
                log.info('入参url:{}'.format(url))
                if '上传文件' in itf_name:
                    resp = submit_files.submit_jpg_file()
                else:
                    resp = base_pages.request_main(method, url, data, header)
                log.info('返回报文:{}'.format(resp))
                log.info('返回报文类型:{}'.format(type(resp)))
                if itf_name == '登录接口':
                    """登录接口向header的Authorization写入最新token"""
                    write_header_value(resp)
                time.sleep(3)
                resp1 = json.loads(resp)
                """报文转换成json，获取code和msg"""
                natrue_code = resp1['code']
                natrue_msg = resp1['msg']
                if check_method == 'code':
                    try:
                        self.assertEqual(natrue_code, '0', msg='code验证')
                        log.info('code验证通过')
                        handleExcel().input_excel_value(i, 10, '通过')
                        if len(resp) > 3000:
                            handleExcel().input_excel_value(i, 12, '报文存入json文件，请查看result目录中接口同编码文件！')
                            write_result_value(case_num, resp)
                        else:
                            handleExcel().input_excel_value(i, 12, resp)
                        # if stop_time is not None:
                        #     time.sleep(int(stop_time))
                    except Exception as e:
                        log.info('测试不通过，报错信息:{}'.format(e))
                        handleExcel().input_excel_value(i, 10, 'code验证失败')
                        handleExcel().input_excel_value(i, 12, resp)

                if check_method == 'json':
                    try:
                        self.assertTrue(jsonJudgment.touch_json(resp, exp_result), msg='json验证')
                        log.info('json验证通过')
                        handleExcel().input_excel_value(i, 10, '通过')
                        if len(resp) > 3000:
                            handleExcel().input_excel_value(i, 12, '报文存入json文件，请查看result目录中接口同编码文件！')
                            write_result_value(case_num, resp)
                        else:
                            handleExcel().input_excel_value(i, 12, resp)
                        if stop_time is not None:
                            time.sleep(int(stop_time))
                    except Exception as e:
                        log.info('测试不通过，报错信息:{}'.format(e))
                        handleExcel().input_excel_value(i, 10, 'json验证失败')
                        handleExcel().input_excel_value(i, 12, resp)

                if check_method == 'code+msg':
                    try:
                        self.assertIn(natrue_msg, CodeMsg.code_msg_test(rows_value[5], natrue_code), msg='code+msg验证成功')
                        log.info('code+msg验证成通过')
                        handleExcel().input_excel_value(i, 10, '通过')
                        handleExcel().input_excel_value(i, 12, resp)
                        if stop_time is not None:
                            time.sleep(int(stop_time))
                    except Exception as e:
                        log.info('测试不通过，报错信息:{}'.format(e))
                        handleExcel().input_excel_value(i, 10, 'code+msg验证失败')
                        handleExcel().input_excel_value(i, 12, resp)
            except Exception as e:
                log.info('测试不通过，报错信息:{}'.format(e))
                handleExcel().input_excel_value(i, 10, '运行失败,请查看日志')
        else:
            handleExcel().input_excel_value(i, 10, '')


if __name__ == '__main__':
    unittest.main()
