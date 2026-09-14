from playwright.sync_api import sync_playwright, expect, Page

class AmazonHomePage:

    def __init__(self, page):
        self.signinAccount= page.locator("#nav-link-accountList")

    def clickon_signin_account_btn(self):
        self.signinAccount.click(timeout=6000)
