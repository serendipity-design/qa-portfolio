from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        # 元素定位
        self.title = page.locator(".title")
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.inventory_item_name = page.locator('[data-test="inventory-item-name"]')

        
        self.add_backpack = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.add_bike_light = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.first_price = page.locator('[data-test="inventory-item-price"]').first
        self.remove_buttons = page.locator('button[data-test^="remove-"]')
        self.add_to_cart_buttons = page.locator('button[data-test^="add-to-cart-"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.add_fleece_jacket = page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]')

    def get_title(self):
        return self.title

    def assert_product_page(self):
        # 断言进入商品页面
        expect(self.title).to_have_text("Products")

    def add_backpack_to_cart(self):
        # 添加背包商品
        self.add_backpack.click()

    def add_to_first_item(self):
        # 添加第一个商品到购物车
        self.add_to_cart_buttons.first.click()
 
    def add_bike_light_to_cart(self):
        # 添加自行车灯
        self.add_bike_light.click()

    def add_fleece_jacket_to_cart(self):
        # 添加抓绒夹克
        self.add_fleece_jacket.click()

    def assert_cart_badge(self, num: str):
        # 断言购物车角标数字
        expect(self.cart_badge).to_have_text(num)

    def go_to_cart(self):
        # 点击进入购物车
        self.cart_link.click()

    def assert_item_count(self, count: int):
        # 断言购物车内商品数量
        expect(self.inventory_item_name).to_have_count(count)

    def sort_by(self, option: str):
        # 选择排序方式
        """option: "az" / "za" / "lohi" / "hilo" """
        self.sort_dropdown.select_option(option)

    def assert_first_price(self, price: str):
        # 断言第一个商品价格
        expect(self.first_price).to_have_text(price)

    def remove_first_item(self):
        # 移除第一个商品
        self.remove_buttons.first.click()

    def logout(self):
        # 登出
        self.page.locator("#react-burger-menu-btn").click()
        self.page.locator('[data-test="logout-sidebar-link"]').click()