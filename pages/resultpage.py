from playwright.sync_api import expect


class AmazonResultPage:

	def __init__(self, page):
		#self.page = page
		self.searchResultLabel = page.locator("span.a-color-state").first
		self.productResults = page.locator("div[data-component-type='s-search-result']")

	def validateSearchResultsPage(self, searchTerm):
		#expect(self.page).to_have_url("**/s?k=**")
		expect(self.searchResultLabel).to_contain_text(searchTerm, ignore_case=True)

	# def getProductResultCount(self):
	# 	return self.productResults.count()

	# def addThirdProductToCart(self):
	# 	cartEligibleResults = self.productResults.filter(
	# 		has=self.page.locator("input[name='submit.add-to-cart']")
	# 	)
	# 	thirdProduct = cartEligibleResults.nth(2)
	# 	addToCartButton = thirdProduct.locator(
	# 		"input[name='submit.add-to-cart']:visible, button:has-text('Add to cart'):visible"
	# 	).first
	# 	expect(addToCartButton).to_be_visible()
	# 	addToCartButton.scroll_into_view_if_needed()
	# 	addToCartButton.click()
	# 	expect(self.page.get_by_role("button", name="1 in cart", exact=True)).to_be_visible()

	# def openFourthProductInNewWindow(self):
	# 	fourthProduct = self.productResults.nth(3)
	# 	productLink = fourthProduct.locator("h2 a").first

	# 	with self.page.context.expect_page() as popupInfo:
	# 		productLink.click(modifiers=["Control"])

	# 	productPage = popupInfo.value
	# 	productPage.wait_for_load_state("domcontentloaded")
	# 	return productPage
