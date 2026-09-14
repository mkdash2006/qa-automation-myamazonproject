import pytest
from playwright.sync_api import Page

from pages.homepage import AmazonHomePage
from pages.resultpage import AmazonResultPage
from pages.shoppingcartpage import ShoppingCartPage


@pytest.mark.smoke1
def test_search_for_iphone(page: Page, navigate_to_amazon):
	search_term = "iPhone"
	home_page = AmazonHomePage(page)
	result_page = AmazonResultPage(page)

	home_page.searchForProduct(search_term)
	home_page.clickCartIcon()

	shopping_cart_page = ShoppingCartPage(page)
	shopping_cart_page.validateShoppingCartTitle()
######
	#result_page.validateSearchResultsPage(search_term)
	# assert result_page.getProductResultCount() > 0, "No iPhone products were displayed"
	# result_page.addThirdProductToCart()

	# product_page = result_page.openFourthProductInNewWindow()
	# assert product_page != page, "The fourth product did not open in a new window"

	# page_title = product_page.title()
	# assert page_title, "The fourth product page title is empty"
	# print(f"Opened fourth product page title: {page_title}")
#######