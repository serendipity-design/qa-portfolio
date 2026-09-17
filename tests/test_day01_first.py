"""
Day 1 —— 你的第一行测试代码。

这是整个项目的起点。目标只有一个：让你在今晚看到终端里出现绿色的 "passed"。

运行方式（在 qa-portfolio 目录下，虚拟环境已激活时）：

    pytest tests/test_day01_first.py -v

看到 8 passed 就算 Day 1 完成。

为什么是 8 条：4 个独立的 test_ 函数，其中 test_add_multiple_cases 因为
带了 4 组 parametrize 数据会自动展开成 4 条 —— 这就是参数化的威力。
"""

import pytest


# ---------------------------------------------------------------
# 被测试的代码（后面你会把它换成真正的业务函数）
# ---------------------------------------------------------------
def add(a, b):
    """两数相加"""
    return a + b


def divide(a, b):
    """两数相除，除数为 0 时抛出 ValueError"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def is_even(n):
    """判断是否为偶数"""
    return n % 2 == 0


# ---------------------------------------------------------------
# 测试用例
# ---------------------------------------------------------------
def test_add_positive_numbers():
    """正常场景：正数相加"""
    assert add(1, 2) == 3


def test_add_negative_numbers():
    """边界/异常场景：负数相加"""
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (0, 0, 0),
        (100, 200, 300),
        (-5, 5, 0),
    ],
)
def test_add_multiple_cases(a, b, expected):
    """数据驱动：一组用例跑 4 遍，这是 pytest 最核心的用法"""
    assert add(a, b) == expected


def test_divide_by_zero_raises():
    """异常场景：验证异常被正确抛出

    pytest.raises 是测试工程师的高频考点，必须会用。
    """
    with pytest.raises(ValueError):
        divide(10, 0)


def test_is_even():
    """等价类划分的练习：偶数类的代表值"""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True


# ---------------------------------------------------------------
# Day 2 的作业：照着上面的写法，给 divide() 也补一组 parametrize 用例
# 提示：至少覆盖 正常相除、除不尽、除数为 0 三种情况
# ---------------------------------------------------------------
