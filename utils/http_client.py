"""HTTP 请求封装（Day 3 会用到）

为什么不直接在用例里写 requests.get()？
因为一旦接口变了、要加鉴权、要统一超时，散落在各处的 requests 调用会让你改到崩溃。
封装这一层，是「脚本」和「自动化框架」的分界线 —— 面试时这点很加分。
"""

import requests
class APIRequestError(Exception):
     """我们自己的异常：网络层面出错时抛出，报错信息更友好"""
     pass

class HttpClient:
    """轻量 HTTP 客户端封装"""

    def __init__(self, base_url, timeout=10, auth_headers=None):
         self.base_url = base_url.rstrip("/")
         self.timeout = timeout
         self.session = requests.Session()
         if auth_headers is not None:
             self.session.headers.update(auth_headers)

    def request(self, method, path, **kwargs):
         """统一入口：拼接 URL、设置超时、返回 Response"""
         url = f"{self.base_url}{path}"
         kwargs.setdefault("timeout", self.timeout)
         try:
             return self.session.request(method, url, **kwargs)
         except requests.exceptions.Timeout:                # ← 填空：超时（提示：Timeout）
             raise APIRequestError(f"请求超时（{self.timeout} 秒）：{url}")
         except requests.exceptions.ConnectionError:                # ← 填空：连不上（提示：ConnectionError）
             raise APIRequestError(f"连接失败，检查网络或地址：{url}")


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


# ================================================================
# Day 3 作业 —— 三步走，做完每一步跑一遍测试确认没改坏：
#   pytest tests/api/test_api_practice.py -v
# ================================================================

# ---------- 第 1 步：自定义异常类（纯抄写，2 行） ----------
# 把下面 3 行复制到文件顶部 import requests 的【正下方】（顶格，不要缩进），
# 然后取消注释。Exception 是所有异常的父类，继承它 = 造一个自己的异常类型。
#
# class APIRequestError(Exception):
#     """我们自己的异常：网络层面出错时抛出，报错信息更友好"""
#     pass


# ---------- 第 2 步：给 __init__ 加 auth_headers（改原方法，填 1 个空） ----------
# 用下面的版本【整体替换】文件里原来的 __init__（第 14~17 行那 4 行）。
# auth_headers=None 的意思：调用方可以不传，不传就不加任何头。
# session.headers.update() 的效果：之后每个请求自动带上这些头。

#     def __init__(self, base_url, timeout=10, auth_headers=None):
#         self.base_url = base_url.rstrip("/")
#         self.timeout = timeout
#         self.session = requests.Session()
#         if auth_headers is not None:
#             self.session.____.update(auth_headers)      # ← 填空（提示：卡片的名字，速查表第 7 条）


# ---------- 第 3 步：给 request() 加异常捕获（改原方法，填 2 个空） ----------
# 用下面的版本【整体替换】文件里原来的 request()。
# 逻辑：正常 → 直接返回；超时/连不上 → 抛我们自定义的异常，报错信息人话。

#     def request(self, method, path, **kwargs):
#         """统一入口：拼接 URL、设置超时、返回 Response"""
#         url = f"{self.base_url}{path}"
#         kwargs.setdefault("timeout", self.timeout)
#         try:
#             return self.session.request(method, url, **kwargs)
#         except requests.exceptions.____:                # ← 填空：超时（提示：Timeout）
#             raise APIRequestError(f"请求超时（{self.timeout} 秒）：{url}")
#         except requests.exceptions.____:                # ← 填空：连不上（提示：ConnectionError）
#             raise APIRequestError(f"连接失败，检查网络或地址：{url}")

# 三个空填完、跑通测试后，可以做附加实验：把 base_url 临时改成
# https://不存在的域名.invalid 跑一次测试，看看自定义报错长什么样，再改回来。

# ================================================================
