import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_page import ProductPage
@pytest.mark.smoke
def test_login_success(page):
    """用例 1:登录成功"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    product_page = ProductPage(page)
    expect(product_page.get_title()).to_have_text("Products")

def test_login_wrong_username(page):
    """用例 2:登录失败 - 用户名错误"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("wrong_user", "secret_sauce")
    login_page.assert_error("Epic sadface: Username and password do not match any user in this service")

def test_login_wrong_password(page):
    """用例 3:登录失败 - 密码错误"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "wrong_password")
    login_page.assert_error("Epic sadface: Username and password do not match any user in this service")

def test_login_empty_username(page):
    """用例 4:登录失败 - 用户名为空"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "secret_sauce")
    login_page.assert_error("Epic sadface: Username is required")

def test_login_empty_password(page):
    """用例 5:登录失败 - 密码为空"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "")
    login_page.assert_error("Epic sadface: Password is required")

def test_login_locked_out_user(page):
    """用例 6:登录失败 - 用户名为 locked_out_user"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")
    login_page.assert_error("Epic sadface: Sorry, this user has been locked out.")
#退出登录
def test_logout(page):
    """用例 7:退出登录"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    product_page = ProductPage(page)
    product_page.logout()
    expect(page.locator("#login-button ")).to_be_visible()