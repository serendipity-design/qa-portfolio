"""pytest 全局 fixture 配置文件（Day 2 会用到）

fixture 是 pytest 最核心的能力：把"准备工作"从用例里抽出来，多个用例复用。
面试常问：「你的自动化框架是怎么复用登录态的？」答案就是 fixture。

放在项目根目录的 conftest.py 会被所有子目录的用例自动加载，不需要 import。
"""

import pytest


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
