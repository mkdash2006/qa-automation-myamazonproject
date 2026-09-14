from playwright.sync_api import sync_playwright, expect, Page

class AmazonHomePage:

    def __init__(self, page):
        #self.page = page
        self.signinAccount= page.locator("#nav-link-accountList")
        self.searchBox = page.locator("#twotabsearchtextbox")
        self.searchButton = page.locator("#nav-search-submit-button")
        self.cartIcon = page.locator("#nav-cart")

    def clickOnSigninAccountBtn(self):
        self.signinAccount.click(timeout=6000)

    def searchForProduct(self, productName):
        self.searchBox.fill(productName)
        self.searchButton.click(timeout=6000)

    def clickCartIcon(self):
        self.cartIcon.click()
