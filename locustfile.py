"""Day 18：用 Locust 压测接口

⚠️ 压测对象只能是「你自己的服务」。绝不要对 jsonplaceholder 这类第三方公共服务压测——
   那等于对别人的服务器发起 DoS 攻击，违反服务条款，也可能违法。
   所以这里压的是本地 mock_server（你自己写的服务）。

用法（开两个终端）：

    # 终端 1：启动被测服务
    python mock_server/app.py

    # 终端 2：启动压测（会开一个 Web 界面）
    locust -f locustfile.py

    # 然后在浏览器打开 http://localhost:8089
    # 填 Number of users（并发数）和 Spawn rate（每秒增加多少用户）→ Start

    Charts 标签页 = TPS 曲线 + 响应时间曲线（任务要看的两个）
    Statistics 标签页 = 请求数 / 失败率 / 平均-中位-P95 响应时间

想不开浏览器、快速跑一轮（无头模式）：

    locust -f locustfile.py --headless -u 10 -r 2 -t 30s
"""

from locust import HttpUser, between, task

TARGET = "http://127.0.0.1:5000"


class MockServerUser(HttpUser):
    """模拟持续调用 /users 接口的用户"""

    host = TARGET

    # 每次请求后等 1~2 秒 —— 模拟真实用户的"思考时间"。
    # 千万别设成 0：那不是真实用户行为，打出来的 TPS 没有参考价值。
    wait_time = between(1, 2)

    @task(3)
    def create_user_success(self):
        """正常创建（权重 3）—— 压的是服务的处理能力"""
        self.client.post(
            "/users",
            json={"id": 10001, "name": "loadtest"},
            name="POST /users (正常)",
        )

    @task(1)
    def create_user_invalid(self):
        """非法入参（权重 1）—— 顺带验证校验分支在压力下也不出错

        注意 catch_response=True：Locust 默认把 HTTP 4xx/5xx 都记成"失败"，
        但这里的 400 是【预期结果】，不是错误。所以要用 catch_response 手动
        把它标记为成功，否则统计里的失败率会虚高。
        这是压测里的经典坑：压测对象的"业务预期"和"HTTP 语义"不是一回事。
        """
        with self.client.post(
            "/users",
            json={"id": -1, "name": "bad"},
            name="POST /users (非法入参)",
            catch_response=True,
        ) as resp:
            if resp.status_code == 400:
                resp.success()          # 400 正是我们要的，算成功
            else:
                resp.failure(f"期望 400，实际 {resp.status_code}")
