"""Day 3 作业⑥：用封装好的 HttpClient 重写 5 个接口请求

第 1 条已写好（直接能跑），剩下 4 条是 TODO，照着抄改。
每写完一条就跑一次：pytest tests/api/test_api_practice.py -v
"""

from utils.http_client import HttpClient


# ---------- 示例：GET 单个帖子（已写好，先跑通它） ----------
def test_get_single_post(base_url):
    client = HttpClient(base_url)
    r = client.get("/posts/1")

    assert r.status_code == 200          # 状态码是 200
    assert r.json()["id"] == 1           # 响应 JSON 里 id 字段等于 1

    client.close()


# ---------- TODO 1：GET 全部帖子 ----------
# 抄示例改 3 处：路径改成 /posts、状态码断言 200、加一条"列表长度大于 0"
# 提示：r.json() 这次返回的是列表，len(r.json()) 是数量

def test_get_all_posts(base_url):
     client = HttpClient(base_url)
     r = client.get("/posts")
     assert r.status_code == 200
     assert len(r.json()) > 0
     client.close()


# ---------- TODO 2：GET 不存在的帖子（反向用例） ----------
# 路径 /posts/999999，断言状态码 404
# 这条的价值：验证系统对"不存在的资源"返回 404 而不是 500——反向用例和正向一样重要

def test_get_missing_post(base_url):
     client = HttpClient(base_url)
     r = client.get("/posts/999999")
     assert r.status_code == 404
     client.close()


# ---------- TODO 3：POST 创建帖子 ----------
# 写法：r = client.post("/posts", json={"title": "foo", "body": "bar", "userId": 1})
# 断言：状态码 201（Created，记住这个和 200 的区别）+ 返回的 title 等于发过去的 "foo"
# 取 JSON 字段：r.json()["title"]

def test_create_post(base_url):
     client = HttpClient(base_url)
     r = client.post("/posts",json={"title": "foo", "body":"bar", "userId": 1})
     assert r.status_code == 201 
     assert r.json()["title"] == "foo"
     client.close()


# ---------- TODO 4：GET 用户列表 ----------
# 路径 /users，断言状态码 200 且数量大于 5

def test_get_users(base_url):
     client = HttpClient(base_url)
     r = client.get("/users")
     assert r.status_code == 200
     assert len(r.json()) > 5
     client.close()
