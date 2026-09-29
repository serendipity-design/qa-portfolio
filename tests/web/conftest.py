"""Web UI 测试的专用配置 —— 只对 tests/web/ 目录生效

为什么放这里而不是项目根目录？
conftest.py 的作用范围是「它所在的目录 + 所有子目录」。
放在 tests/web/ 下，接口测试（tests/api/）就不会被这些配置影响。
这是 pytest 的分层配置机制，面试聊框架结构时可以直接讲。
"""

import os

import pytest

SHOT_DIR = "screenshots"


# ================================================================
# 失败自动截图（Day 9 第 4 项）
#
# 原理：pytest 每执行完一个用例会生成一份「报告对象」，
#       @pytest.hookimpl(...) 让我们在这个报告生成时插一脚，
#       检查"这个用例是不是失败了"，如果是，就用 page 截张图。
# ================================================================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # yield 之前 = 报告还没生成；yield 之后 = 报告已生成，可以拿到结果
    outcome = yield
    report = outcome.get_result()

    # report.when 有三个阶段：setup（准备）/ call（执行）/ teardown（收尾）
    # 只在「执行阶段失败」时截图，避免 setup 报错也触发
    if report.when == "call" and report.failed:

        # 从用例的参数里取出 page 对象（没用 page 的用例就没有，所以要 get）
        page = item.funcargs.get("page")

        if page is not None:
            os.makedirs(SHOT_DIR, exist_ok=True)          # 目录不存在就建一个
            shot_path = os.path.join(SHOT_DIR, f"{item.name}.png")
            page.screenshot(path=shot_path)               # 截图存盘
            print(f"\n[失败截图] 已保存：{shot_path}")     # 打印出来，方便运行时看到
