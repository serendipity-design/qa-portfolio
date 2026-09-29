from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        # 元素定位
        self.title = page.locator(".title")
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.inventory_item_name = page.locator('[data-test="inventory-item-name"]')

        # 两个商品的加入购物车按钮
        self.add_backpack = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.add_bike_light = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')

    def assert_product_page(self):
        # 断言进入商品页面
        expect(self.title).to_have_text("Products")

    def add_backpack_to_cart(self):
        # 添加背包商品
        self.add_backpack.click()

    def add_bike_light_to_cart(self):
        # 添加自行车灯
        self.add_bike_light.click()

    def assert_cart_badge(self, num: str):
        # 断言购物车角标数字
        expect(self.cart_badge).to_have_text(num)

    def go_to_cart(self):
        # 点击进入购物车
        self.cart_link.click()

    def assert_item_count(self, count: int):
        # 断言购物车内商品数量
        expect(self.inventory_item_name).to_have_count(count)