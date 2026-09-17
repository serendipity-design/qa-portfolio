"""HTTP 请求封装（Day 3 会用到）

为什么不直接在用例里写 requests.get()？
因为一旦接口变了、要加鉴权、要统一超时，散落在各处的 requests 调用会让你改到崩溃。
封装这一层，是「脚本」和「自动化框架」的分界线 —— 面试时这点很加分。
"""

import requests


class HttpClient:
    """轻量 HTTP 客户端封装"""

    def __init__(self, base_url, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        """统一入口：拼接 URL、设置超时、返回 Response"""
        url = f"{self.base_url}{path}"
        kwargs.setdefault("timeout", self.timeout)
        return self.session.request(method, url, **kwargs)

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, json=None, **kwargs):
        return self.request("POST", path, json=json, **kwargs)

    def put(self, path, json=None, **kwargs):
        return self.request("PUT", path, json=json, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)

    def close(self):
        self.session.close()


# ---------------------------------------------------------------
# Day 3 作业：
# 1. 给 request() 加上异常捕获：requests.exceptions.Timeout / ConnectionError
#    捕获后 raise 一个你自己定义更清晰的异常，比如 APIRequestError
# 2. 给 HttpClient 加一个 auth_headers 参数，支持统一注入鉴权头
# ---------------------------------------------------------------
