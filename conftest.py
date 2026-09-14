# Fixtures
from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture()
def navigate_to_amazon(page: Page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(5000)
# # If any interim page will come before opening homepage. 
# # eX- timeout page, continue page
#     countofbtns = page.locator('//*[contains(text(),"shopping")]').count()  
#     if countofbtns > 0:
#         page.locator('//*[contains(text(),"Shopping")]').click()