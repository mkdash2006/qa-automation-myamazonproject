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
    home_page_obj.clickon_signin_account_btn()
    signin_page_obj.fill_email_or_mobile_text_field()
    signin_page_obj.click_on_continue_btn()
    signin_page_obj.validate_next_signpage()
    signin_page_obj.fill_password_text_field()
