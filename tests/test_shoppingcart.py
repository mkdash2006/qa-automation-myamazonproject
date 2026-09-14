import pytest
from playwright.sync_api import Page

from pages.homepage import AmazonHomePage
from pages.resultpage import AmazonResultPage
from pages.shoppingcartpage import ShoppingCartPage


@pytest.mark.smoke1
def test_shopping_cart(page: Page, navigate_to_amazon):
	home_page = AmazonHomePage(page)
	shopping_cart_object = ShoppingCartPage(page)

	home_page.clickCartIcon()
	shopping_cart_object.validateShoppingCartTitle()