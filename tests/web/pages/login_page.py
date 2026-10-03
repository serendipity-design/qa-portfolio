#把 saucedemo 拆成两个页面类
from playwright.sync_api import Page, expect
import logging

logger = logging.getLogger(__name__)
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, pwd):
        logger.info(f"登录账号：{user}")
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def assert_error(self,message):
        expect(self.page.locator('[data-test="error"]')).to_have_text(message)