"""边界用例（针对本地 mock 服务 mock_server/app.py）

和 test_ddt.py 的区别：
    test_ddt.py       → 测外部假数据站，只断言 status_code
    test_boundary.py  → 测我们自己实现的服务，额外断言错误提示文案

**不用手动启动服务**：下面那个 fixture 会在后台线程里把 mock 服务拉起来，
测试跑完自动结束。所以直接跑这条命令就行：

    pytest tests/api/test_boundary.py -v
"""

import threading
import time

import pytest
import yaml

from mock_server.app import app as mock_app
from utils.http_client import HttpClient

MOCK_BASE_URL = "http://127.0.0.1:5000"

cases = yaml.safe_load(open("data/boundary_cases.yaml", encoding="utf-8"))


@pytest.fixture(scope="session", autouse=True)
def start_mock_server():
    """在后台线程启动 mock 服务（session 级：整个测试会话只起一次）"""
    server = threading.Thread(
        target=lambda: mock_app.run(
            host="127.0.0.1", port=5000, use_reloader=False, threaded=True
        ),
        daemon=True,
    )
    server.start()
    time.sleep(2)          # 给服务 2 秒启动时间
    yield
    # daemon 线程会随进程结束自动退出


@pytest.mark.parametrize("case", cases, ids=[c["name"] for c in cases])
def test_boundary(case):
    client = HttpClient(MOCK_BASE_URL)
    r = client.post(case["path"], json=case["body"])

    assert r.status_code == case["expected_status"]
    assert r.json()["msg"] == case["expected_msg"]
    assert r.elapsed.total_seconds() < 2
    client.close()
