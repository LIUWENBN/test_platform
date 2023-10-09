import time
import unittest
import sys
import os
from time import sleep

"""在jenkins上配置环境变量和自定义变量后，仍可能返回找不到工程的包,需要导入工程地址，如下："""
sys.path.append("/")
from bcpinterface.basePage.HTMLTestRunner import HTMLTestRunner
from bcpinterface.handles.email_script import send_email
from bcpinterface.handles.handle_zipfile import pack_file
from bcpinterface.handles.handle_file_name import del_files


class Run:

    def run_case(self):
        del_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd()))+'/report/')
        del_files(del_path)
        run_case_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/runScript/')
        discover = unittest.defaultTestLoader.discover(run_case_path, pattern='test*.py')
        current_time = time.strftime("%Y-%m-%d %H_%M_%S")
        report_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/report/htmlReport')
        file_name = report_path + '/接口测试报告' + current_time + '.html'
        with open(file_name, 'wb') as fp:
            runner = HTMLTestRunner(stream=fp, title='接口测试报告', description='接口测试情况')
            runner.run(discover)
        sleep(20)
        pack_file(current_time)
        sleep(5)
        send_email()
        sleep(15)


if __name__ == '__main__':
    Run().run_case()
