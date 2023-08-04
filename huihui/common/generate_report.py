import argparse
import os
import time
import unittest
from datetime import datetime

from XTestRunner import HTMLTestRunner

current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
folder_todaytime = datetime.today().strftime("%Y-%m-%d")
report = r'.\reports\\' + folder_todaytime + '\\' + current_time + 'report.html'
runner = HTMLTestRunner()
suit = unittest.TestSuite()


def add_test_case(Case):
    for test in Case:
        suit.addTest(unittest.makeSuite(test))
    return suit


def makedirs_folder():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Run test cases.')
    parser.add_argument('--output', metavar='PATH', default='reports/', help='The path to output test reports.')
    args = parser.parse_args()

    folder = os.path.exists(r'.\reports\\' + folder_todaytime)
    if not folder:
        os.makedirs(r'.\reports\\' + folder_todaytime)
        print("---  新建文件夹成功! ---")
    else:
        print("---  文件夹已存在!  ---")


def generate_report():
    # 可自定义测试报告文件名
    print(report)
    with(open(report, 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='pyramid',  # 报告中右上角标题名
            tester='冯慧慧',  # 测试人员
            description=['pass接入pyramid项目测试报告'],  # 测试报告描述
            language="zh-CN"
        )
        runner.run(suit)
    return report


def send_email(re):
    runner.send_email(
        user='jiangyouw163@163.com',  # 发送的邮箱
        password="WBEDJECUNAQLMYLP",  # 授权码，不是密码！！！qq:mbnskdrlxndmbdeb;163:WBEDJECUNAQLMYLP
        host='smtp.163.com',  # 默认就好，若不是用的qq邮箱，则...自己百度
        to='fenghuihui_vendor@sensetime.com',  # 接收邮箱
        attachments=re,
        ssl=True)
