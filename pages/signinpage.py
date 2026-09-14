from playwright.sync_api import sync_playwright, expect, Page
from utils import jsonhandling
from utils import csvhandling
from utils.csvhandling import csvhandling
from utils.jsonhandling import jsonhandling


class SignInHome:

    def __init__(self, page):
        self.emailOrMobileTextField= page.locator("input[name='email']")
        self.continueBtn= page.locator("#continue")
        self.passwordTextField= page.locator("#ap_password") 
        self.signinSubmitBtn= page.locator("input#signInSubmit")
        self.otpCodeTextField= page.locator("input#input-box-otp")
        self.submitCodeBtn= page.locator("input.a-button-input")
        self.passwordTextField= page.locator("#ap_password")  

    def fill_email_or_mobile_text_field(self):
        #json data
        json_data = jsonhandling('testdata\\creds.json')  
        self.emailOrMobileTextField.fill(json_data["positivedata"]["email"]) 
        # #csv data
        # csv_data = csvhandling("testdata\\creds2.csv")
        # self.emailOrMobileTextField.fill(csv_data[0]["email"], timeout=6000)

    def fill_password_text_field(self):
        #json data
        json_data = jsonhandling('testdata\\creds.json') 
        self.passwordTextField.fill(json_data["positivedata"]["password"])
        # #csv data
        # csv_data = csvhandling("testdata\\creds2.csv")
        # self.password_text_field.fill(csv_data[0]["password"], timeout=6000)

    def click_on_continue_btn(self):
        self.continueBtn.click()              

    def validate_next_signpage(self):
        # Verify that the next sign-in step is displayed
        expect(self.passwordTextField).to_be_visible(timeout=6000)  # Adjust the timeout as needed
    