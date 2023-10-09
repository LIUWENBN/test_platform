# coding = utf-8
import time
from requests.utils import dict_from_cookiejar
import requests


class base_script(object):
    def request_post(self, url, data, header=None):
        """post请求"""
        response = requests.post(url=url, data=data, headers=header)
        res = response.text
        return res

    def request_get(self, url, data, header=None):
        """get请求"""
        response = requests.get(url=url, params=data, headers=header)
        res = response.text
        return res

    def request_delete(self, url, data, header=None):
        response = requests.delete(url=url, data=data, headers=header)
        res = response.text
        return res

    def request_put(self, url, data, header=None):
        response = requests.put(url=url, data=data, headers=header)
        res = response.text
        return res

    def request_main(self, method, url, data, header=None):
        if method == 'POST':
            res = self.request_post(url, data, header)
        elif method == 'GET':
            res = self.request_get(url, data, header)
        elif method == 'DELETE':
            res = self.request_delete(url, data, header)
        else:
            res = self.request_put(url, data, header)
        return res


base_request = base_script()
