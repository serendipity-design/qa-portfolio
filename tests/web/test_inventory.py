"""商品列表 / 购物车相关用例"""
import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.product_page import ProductPage


def _login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

@pytest.mark.smoke
def test_inventory_count(page):
    _login(page)
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_count(6)

def test_sort_by_price_low_to_high(page):
    """用例 7：价格从低到高排序"""
    _login(page)
    product_page = ProductPage(page)
    product_page.sort_by("lohi")
    product_page.assert_first_price("$7.99")

@pytest.mark.smoke
def test_add_one_item(page):
    _login(page)
    product_page = ProductPage(page)
    product_page.add_to_first_item()
    product_page.assert_cart_badge("1")

def test_add_two_then_remove_one(page):
    """用例 9：加购 2 件 → 角标 2；移除 1 件 → 角标 1"""
    _login(page)
    product_page = ProductPage(page)
    product_page.add_backpack_to_cart()
    product_page.add_bike_light_to_cart()
    product_page.assert_cart_badge("2")

    product_page.remove_first_item()
    product_page.assert_cart_badge("1")


def test_cart_shows_added_item(page):
    """用例 10：加购后进购物车，显示 1 件商品"""
    _login(page)
    product_page = ProductPage(page)
    product_page.add_backpack_to_cart()
    product_page.go_to_cart()
    product_page.assert_item_count(1)