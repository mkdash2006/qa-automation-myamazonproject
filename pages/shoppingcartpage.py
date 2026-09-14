from playwright.sync_api import expect


class ShoppingCartPage:

	def __init__(self, page):
		self.page = page

	def validateShoppingCartTitle(self):
		expect(self.page).to_have_title("Amazon.in Shopping Cart", timeout=6000)
