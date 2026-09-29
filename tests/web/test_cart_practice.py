"""Day 9 第 5 项：saucedemo「加购物车」完整流程用例

目标：走完 登录 → 加购 → 校验角标 → 进购物车 → 校验件数 这条链路。

┌─ 先做第 1 步：用录制器拿到真实定位器 ────────────────────┐
│  在项目根目录、venv 激活状态下跑：                        │
│      playwright codegen https://www.saucedemo.com         │
│  会弹出「浏览器 + 代码窗口」。在浏览器里手动走一遍：        │
│     登录 standard_user / secret_sauce → 点第一个商品的      │
│     Add to cart → 点右上角购物车图标                       │
│  代码窗口会实时生成每一行的定位器，直接复制过来填下面的空。 │
└──────────────────────────────────────────────────────────┘

找不到元素时，还可以按 F12 打开开发者工具，用左上角的箭头
点元素，看 Elements 面板里的 id / class 是什么。
"""

from playwright.sync_api import Page
from tests.web.pages.login_page import LoginPage
from tests.web.pages.product_page import ProductPage

def test_add_to_cart_flow(page: Page):
    # 实例化页面对象
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    # 1.打开登录页+登录
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # 2.验证进入商品页，加第一个商品
    product_page.assert_product_page()
    product_page.add_backpack_to_cart()

    # 3.断言角标为1
    product_page.assert_cart_badge("1")

    # 4.进入购物车，断言商品数量1
    product_page.go_to_cart()
    product_page.assert_item_count(1)


def test_add_two_items_to_cart(page: Page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # 添加两件商品
    product_page.add_backpack_to_cart()
    product_page.add_bike_light_to_cart()

    product_page.assert_cart_badge("2")
    product_page.go_to_cart()
    product_page.assert_item_count(2)
# ---------------------------------------------------------------
# 写完后跑：
#     pytest tests/web/test_cart_practice.py -v --headed
#
# 加 --headed 就能亲眼看到浏览器把整个过程走一遍。
#   再写一条反向用例 —— 加两件不同商品，断言角标是 "2"、
#   购物车里有 2 条记录。正向 + 反向成对，是你简历里能讲的细节。
# ---------------------------------------------------------------
