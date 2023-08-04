"""
@Time:2023/8/3 17:34
@Author:jiangyouwen.vendor
Don't quit!
"""
import time

class Test_case_01:

    def test_01_ceshi(self):
        loca = time.strftime("%y%m%d%H%M",time.localtime())
        print(str(loca))
