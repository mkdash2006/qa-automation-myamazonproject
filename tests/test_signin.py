from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.signinpage import SignInHome
from pages.homepage import AmazonHomePage
from utils.jsonhandling import jsonhandling
from utils.csvhandling import csvhandling

@pytest.mark.smoke
def test_signin(page:Page, navigate_to_amazon):
    home_page_obj= AmazonHomePage(page)
    signin_page_obj= SignInHome(page)
    home_page_obj.clickOnSigninAccountBtn()
    signin_page_obj.fillEmailOrMobileTextField()
    signin_page_obj.clickOnContinueBtn()
    signin_page_obj.validateNextSignPage()
    signin_page_obj.fillPasswordTextField()
