import json
import time
import unittest

import requests

loca = str(time.strftime("%y%m%d%H%M", time.localtime()))  # 取一个日期时间,作为后面的用户名使用


class Test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RlIjoiNjcxOCIsInVzZXJfbmFtZSI6ImRlbmd3ZW5ibyIsInNvdXJjZSI6MSwidHlwZSI6MSwidXNlcklkIjo5MTk5LCJhdXRob3JpdGllcyI6WyJ1c2VyIl0sImNsaWVudF9pZCI6InN1ZXoiLCJzY29wZSI6WyJBbGwiXSwid2V3b3JrSWQiOiJkd2IuIiwid2VjaGF0SWQiOiJjNDg2NWU4Yy1kYzlmLTQ3YTEtYjBlZS0zNTg3Y2M1ZGZhMGYiLCJmdWxsbmFtZSI6IumCk-aWh-WNmiIsImV4cCI6MTY5MTEyMjc1NywianRpIjoiNzA3NDQ5MGEtZmNmYy00NzYxLTlhMjYtNGFmMmFlYzNhZDM0Iiwic3RhdHVzIjoxfQ.SJ5kstBlnr5S0YMFQad1PUhW1sY5kUhpjhhR3jglLPpObQ-RS-giFQMaAPx7VK2CAxqm89d9M6fmyZZdV5c0jbs1JGdIjthxb7Uir24rnUXHtqnTuYkZKYr8fKXf-dwNm5FrQJIHfRu1yhoRfM5TMRkZBxFF5wzlUbSzeCRqyvsM2aRhItrkxJcbLv52PQ3WrqWUVs74CWrYWQ4FJbmQvLR0oe5IoYfm5NWNAtkJ3a9jLFnqGJ11TDqoLEHWQvuNQPj-MDcUwLtjLm3geHsd09BqPI_VyrPle7USx1yV7u13yai1d4DKbl1rqtQgMaiz0RhErWCySGMOoAjkHE6-ig"

    def test_01_get_token(self):
        """获取token接口"""
        jsons = {"password": "Pyramid@CIT123",
                 "username": "dengwenbo"
                 }
        headers = {"Content-Type": "application/json"}
        response = requests.post("https://suez-test-in.sensetime.com/api/userCenter/v1/login/getToken", json=jsons, headers=headers)
        data = json.loads(response.text)
        self.__class__.token = data['data']['token']
        print(f"Response Body :{response.text}")
        print(f"requests Body :{response.request.body}")
        print(f"token:{self.token}")
        assert response.status_code == 200
        assert "success" in response.text

    def test_02_strateg(self):
        """根据id查询通行策略"""
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.__class__.token}"}
        strategy = requests.get("https://suez-test-in.sensetime.com/api/khufu/v1/rule/14", headers=headers)  # 14是指定的id
        print(f"test_strategy_02 Response Body :{strategy.text}")
        print(f"test_strategy_02 requests Body :{strategy.request.body}")
        assert strategy.status_code == 200
        assert "success" in strategy.text

    def test_03_add_visitor_group(self):
        """新增访客组"""
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.__class__.token}"}
        jsons = {
            "groupName": f"{str(loca)}",  # 访客组唯一,使用后需要删除, 使用时间代替
            "remark": "autodriver"
        }
        add_visitor_group = requests.post("https://suez-test-in.sensetime.com/api/userCenter/v1/visitor/group/add", json=jsons, headers=headers)
        print(f"add_visitor_group Response Body :{add_visitor_group.text}")
        print(f"add_visitor_group requests Body :{add_visitor_group.request.body}")
        assert add_visitor_group.status_code == 200
        assert "success" in add_visitor_group.text

    def test_04_add_visitor(self):
        """新增访客"""
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.__class__.token}"}
        jsons = {
            "idType": 0,
            "gender": 0,
            "purpose": "string",
            "mobile": "18778013415",
            "timeZone": "GMT+8",
            "remark": "来访人员",
            "avatar": "c0f7ec3e-7ede-4df1-bd9f-1e0c3f424972",
            "userName": f"{str(loca)}",  # 访客唯一,使用后需要删除,使用时间代替
            "idNo": "jiangyouwen",
            "areaCode": "86",
            "groupIds": [
                0
            ],
            "startTime": 0,
            "endTime": 0,
            "email": "jiangyouw163@163.com",
            "status": "true"
        }
        add_visitor = requests.post("https://suez-test-in.sensetime.com/api/userCenter/v1/visitor/add", json=jsons, headers=headers)
        print(f"add_visitor Response body: {add_visitor.text}")
        print(f"add_visitor requests code:{add_visitor.status_code}")
        assert add_visitor.status_code == 200

    def test_05_license_upload(self):
        """license上传"""
        headers = {"Content-Type": "multipart/form-data",
                   "file": "@BORCA DFF4F7CA-0D99-4AEC-BOF1-877B92628B24.lic",
                   "Authorization": f"Bearer {self.__class__.token}"}
        with open(r"C:\Users\jiangyouwen.vendor\Downloads\BORCA_DFF4F7CA-0D99-4AEC-B0F1-877B92628B24.lic", 'rb') as files:  # 注意文件路径,需要修改
            files = {"file": files}
            license_upload = requests.post("https://suez-test-in.sensetime.com/api/license/v1/license/file/upload", headers=headers, files=files)
        print(f"license_upload Response body : {license_upload.text}")
        print(f"license_upload requests body : {license_upload.request.body}")
        print(f"license_upload requests headers : {license_upload.request.headers}")
        print(f"license_upload requests code: {license_upload.status_code}")
        assert "success" in license_upload.text

    def test_06_device_base_controller(self):
        """新增设备"""
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {self.__class__.token}",
                   "Accept-Language": "zh-CN"
                   }
        jsons = {
            "password": "12345678",
            "port": 8000,
            "ip": "10.9.144.3",
            "name": "测试设备",
            "remark": "autodriver-01",
            "username": "admin"
        }
        device_base_controller = requests.post("https://suez-test-in.sensetime.com/api/khufu/v1/device/base", headers=headers, json=jsons)
        print(f"device_base_controller response body : {device_base_controller.text}")
        print(f"device_base_controller Requests body : {device_base_controller.request.body}")
        print(f"device_base_controller requests headers : {device_base_controller.request.headers}")
        print(f"device_base_controller requests code: {device_base_controller.status_code}")
