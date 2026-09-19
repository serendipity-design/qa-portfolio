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


# ================================================================
# Day 2 作业② —— 给 divide() 补一组 parametrize 用例
# 三步走，每做完一步就跑一次：pytest tests/test_day01_first.py -v
# ================================================================

# ---------- 第 1 步：最笨的写法（不用 parametrize） ----------
# 我已经写好 1 条，你【照着抄 3 条】。目的：体感"重复"这件事。


# ---------- 第 2 步：观察（不用动手） ----------
# 你会发现这 4 个函数长得一模一样，唯一区别是 3 个数字。
# 【相同】的部分 → 留在函数里
# 【不同】的部分（10,2,5.0 这三样）→ 抽到数据表格里
# 这就是 parametrize 的全部思想：一个函数 + 一张数据表 = N 条用例。


# ---------- 第 3 步：合并成一个 parametrize 函数（填空） ----------
# 把表格里的 ____ 补成数字（把第 1 步的数字按 (a, b, expected) 搬进来），
# 然后删掉下面每行开头的 "# " 注释符，保存再跑。

@pytest.mark.parametrize(
     "a, b, expected",
     [
         (10, 2, 5.0),
         (9, 4, 2.25),
         (0, 5, 0.0),
         (-10, 2, -5.0),
     ],
 )
def test_divide_normal(a, b, expected):
     assert divide(a, b) == expected


# ---------- 第 4 步：除数为 0（照抄现成例子改数据） ----------
# 除数为 0 不返回值而是抛异常，所以不能放进 expected 表格，要单独写。
# 参考 test_divide_by_zero_raises 的写法，填空后取消注释：

@pytest.mark.parametrize(
     "a, b",
     [
         (10, 0),
         (5, 0),
         (0, 0),
     ],
 )
def test_divide_by_zero_multiple(a, b):
     with pytest.raises(ValueError):
         divide(a, b)


