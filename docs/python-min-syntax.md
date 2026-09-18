# 读懂这个项目需要的 Python 最小语法

> 这不是 Python 教程。这是**恰好够读懂本项目代码**的最小语法集，全部例子都来自你自己的代码。
> 用法：看不懂哪段代码 → 来这里查对应概念 → 回去继续。
> 完整文档兜底：[菜鸟教程 Python3](https://www.runoob.com/python3/python3-tutorial.html)，只查不啃。

---

## 1. 变量：给数据起个名字

```python
base_url = "https://jsonplaceholder.typicode.com"   # 等号是"把右边的值存进左边的名字"
timeout = 10
```

## 2. 函数：把一段代码打包，起个名字

```python
def add(a, b):        # def 定义函数；a、b 是参数（从外面传进来的值）
    return a + b      # return 把结果交还给调用者
```

调用就是喊它的名字并传值：

```python
result = add(1, 2)    # result 现在是 3
```

**测试函数的唯一区别**：名字必须以 `test_` 开头，pytest 靠这个名字找到它们。

## 3. 比较：== 是"等于吗"，= 是"存进去"

```python
a = 5        # 把 5 存进 a
a == 5       # 问：a 等于 5 吗？返回 True 或 False
```

`=` 是赋值，`==` 是判断。**初学 90% 的 bug 来自把这两个搞混。**

## 4. assert：测试的灵魂

```python
assert add(1, 2) == 3
```

翻译成人话：**"我断言 add(1, 2) 的结果是 3。如果真是，什么都不发生；如果不是，测试失败并报错。"**

所有自动化测试，本质上就是一串 assert。

## 5. 列表 list：一排东西，用方括号

```python
cases = ["登录成功", "密码错误", "账号锁定"]
cases[0]        # 第 1 个：注意编号从 0 开始
len(cases)      # 数量：3
```

## 6. 元组 tuple：不可改的列表，用圆括号

```python
(1, 1, 2)       # 三个值捆在一起，就是 parametrize 表格里的一行
```

`(1, 1, 2)` 和 `[1, 1, 2]` 长得像，区别是元组创建后不能改。**在 parametrize 里约定俗成用元组。**

## 7. 字典 dict：键值对，像一张卡片

```python
headers = {
    "User-Agent": "qa-portfolio/1.0",
    "Content-Type": "application/json",
}
headers["Content-Type"]        # 取出 "application/json"
```

这就是 `default_headers` fixture 要返回的东西——一张写着请求头的卡片。

## 8. 字符串与 f-string

```python
name = "登录"
count = 30
msg = f"共 {count} 条{name}用例"    # f 开头 + 花括号里放变量 → "共 30 条登录用例"
```

## 9. import：用别人写好的功能

```python
import requests                        # 导入整个模块
from utils.http_client import HttpClient   # 从我们的文件里导入某个类

r = requests.get(base_url)             # 用"模块名.功能"的方式调用
```

`pytest`、`requests` 都是别人写好的库，import 之后才能用。

## 10. 异常：出错的两种姿势

```python
raise ValueError("除数不能为 0")     # 主动抛出错误："这里有问题，立刻停下"

with pytest.raises(ValueError):      # 断言"这里应该会出错"
    divide(10, 0)                    # 如果它真的抛了 ValueError → 测试通过
```

测试里常考的反直觉点：**验证"会报错"也是一种测试用例。**

## 11. for 循环：把列表里每个都过一遍

```python
for case in cases:
    print(case)          # 列表里有几个元素就执行几次，case 依次是每个元素
```

parametrize 本质上就是 pytest 替你写了这个循环。

## 12. 装饰器 @：贴在函数上的标签

```python
@pytest.mark.parametrize(...)
def test_xxx(): ...
```

`@xxx` 的意思是"**给下面的函数贴一个标签，pytest 看到标签会对它做特殊处理**"。

现阶段你不需要理解装饰器的实现原理（那涉及函数也是对象这种进阶概念），只需要记住三个标签的作用：

| 标签 | 作用 |
|------|------|
| `@pytest.mark.parametrize` | 用表格数据反复喂给函数 |
| `@pytest.fixture` | 标记这是个"准备工作"，别的用例可以借用 |
| `@pytest.mark.smoke` | 给用例分组，`pytest -m smoke` 只跑标了这组的 |

---

## 检验：现在回头再读一遍 Day 1 的代码

```python
@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (0, 0, 0)])
def test_add_multiple_cases(a, b, expected):
    assert add(a, b) == expected
```

如果现在的你能说出 —— "贴了表格标签的测试函数，pytest 把每行数据按表头喂给参数，执行 assert，不对就失败" —— **你已经读懂了 80% 的项目代码**。

剩下的 20% 是 requests 怎么发请求（Day 2-3 现场学）和 Playwright 怎么操作浏览器（Day 8 现场学）。**都是用到再学。**

---

## Day 2 两道作业的提示（卡住再看）

**作业 ①（default_headers）**：打开 `conftest.py`，拉到最底部的注释——**答案就在那里**，你的任务是取消注释、保存、跑一遍，确认没打错字。看懂 dict 的每一行在干嘛（见上面第 7 条）。

**作业 ②（给 divide 补 parametrize）**：照抄 test_add_multiple_cases 的结构，换数据：

- 正常相除：`(10, 2, 5.0)`、`(9, 4, 2.25)` —— 注意除法结果带小数点
- 被除数为 0：`(0, 5, 0.0)`
- 负数：`(-10, 2, -5.0)`
- **除数为 0 的别放进 expected 表格里**——它不返回值，是抛异常，要用 `pytest.raises` 单独写（见第 10 条，Day 1 的 `test_divide_by_zero_raises` 就是现成例子）
