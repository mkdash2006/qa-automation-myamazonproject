import pytest
from playwright.sync_api import Page

from pages.homepage import AmazonHomePage
from pages.resultpage import AmazonResultPage
from pages.shoppingcartpage import ShoppingCartPage
from pages.signinpage import SignInHome

@pytest.mark.smoke1
def test_search_results(page: Page, navigate_to_amazon):
	home_page = AmazonHomePage(page)
	shopping_cart_obj = ShoppingCartPage(page)
	signin_page_obj= SignInHome(page)
	search_result_obj = AmazonResultPage(page)

	home_page.searchForProduct("iPhone")
	search_result_obj.validateSearchResultsPage("iPhone")