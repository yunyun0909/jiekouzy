import unittest
# from read_config import Readconfig
import pytest
import requests
from ddt import ddt, file_data

# r = Readconfig()

from test_api.test_zy_yaml.read_config import Readconfig


@ddt
class TestToken:
    # 使用ddt里的@file_data读取yaml文件,并将yaml文件自动传入使用了@file_data的函数中，
    # 因此，函数设置了**kwa不定长关键字参数来接收数据
    @file_data("config.yaml")
    # @pytest.mark.parametrize("data",Readconfig("config.yaml").read_yaml())
    def test_get_token(self, **kwa):
        print(kwa)
        # print("从yaml文件获取额数据：",data)
        # url= "http://39.106.51.187:8080/login"
        # dat = {"username":"17629041024",
        #        "password":"050902"}
        # resp = requests.request("post",url=url,data=dat)
        # a = resp.json()
        # b = a["code"]
        # print(a)
        # assert b == 0
        # print(kwa,type(kwa))  #会得到一个字典
        mothod = kwa["request"]["mothod"]
        url = kwa["request"]["url"]
        dat = kwa["request"]["params"]
        head = kwa["request"]["headers"]
        # print(head)
        resp = requests.request(method=mothod, url=url, data=dat)
        a = resp.json()
        # print(a)
        assert kwa["validate"][0]["equals"]["code"] == a["code"]
        # print(a["code"])
        # print(kwa["validate"][0]["equals"]["code"])
        # for i in range(len(kwa)):
        #     print(i)
        #     # for a in kwa[i]:
        #     #     print(a)

    @pytest.mark.parametrize("da", Readconfig("config.yaml").read_yaml())
    def test_token02(self, da):
        url = da["request"]["url"]
        meth = da["request"]['mothod']
        dat = da["request"]['params']
        req = requests.request(method=meth, url=url, data=dat)
        a = req.json()
        assert da["validate"][0]["equals"]["code"] == a["code"]


if __name__ == "__main__":
    pytest.main(["-v"])
