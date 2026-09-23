"""pytest 全局 fixture 配置文件（Day 2 会用到）

fixture 是 pytest 最核心的能力：把"准备工作"从用例里抽出来，多个用例复用。
面试常问：「你的自动化框架是怎么复用登录态的？」答案就是 fixture。

放在项目根目录的 conftest.py 会被所有子目录的用例自动加载，不需要 import。
"""

import pytest

from utils.http_client import HttpClient


@pytest.fixture(scope="session")
def base_url():
    """被测系统的基础地址。

    改成你自己的练手目标即可，推荐先用这个免费假接口站：
    https://jsonplaceholder.typicode.com
    """
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_timeout():
    """统一的接口超时时间（秒）"""
    return 10


@pytest.fixture(scope="session")
def http_client(base_url, api_timeout):
    """全局唯一的 HTTP 客户端实例。

    用例里只要在参数里写 http_client，pytest 就会自动把这里造好的实例递进来，
    整个测试会话共用一个连接，跑完自动关闭。
    （Day 6 的 test_ddt.py 用的就是它——之前缺了这个定义，15 条用例集体 ERROR）
    """
    client = HttpClient(base_url, timeout=api_timeout)
    yield client          # yield 之前的 = 准备工作；之后的 = 收尾工作
    client.close()


# ---------------------------------------------------------------
# Day 2 作业：自己写一个 fixture
# 目标：返回一个 dict 形式的请求头，让后续所有接口用例都能复用
#
# @pytest.fixture(scope="session")
# def default_headers():
#     return {
#         "User-Agent": "qa-portfolio/1.0",
#         "Content-Type": "application/json",
#     }
# ---------------------------------------------------------------
@pytest.fixture(scope="session")
def default_headers():
    """统一的请求头"""
    return {
        "User-Agent": "qa-portfolio/1.0",
        "Content-Type": "application/json",
    }
