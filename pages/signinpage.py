from playwright.sync_api import sync_playwright, expect, Page
from utils import jsonhandling
from utils import csvhandling
from utils.csvhandling import csvhandling
from utils.excelhandling import excelhandling
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

    def fillEmailOrMobileTextField(self):
        # #json data
        # json_data = jsonhandling('testdata\\creds.json')  
        # self.emailOrMobileTextField.fill(json_data["positivedata"]["email"]) 
        # #csv data
        # csv_data = csvhandling("testdata\\creds2.csv")
        # self.emailOrMobileTextField.fill(csv_data[0]["email"], timeout=6000)
        # excel data
        excel_data = excelhandling('testdata\\sample_creds.xlsx')
        self.emailOrMobileTextField.fill(excel_data[4][0], timeout=60000)

    def fillPasswordTextField(self):
        # #json data
        # json_data = jsonhandling('testdata\\creds.json') 
        # self.passwordTextField.fill(json_data["positivedata"]["password"])
        # #csv data
        # csv_data = csvhandling("testdata\\creds2.csv")
        # self.password_text_field.fill(csv_data[0]["password"], timeout=6000)
        # excel data
        excel_data = excelhandling('testdata\\sample_creds.xlsx')
        self.passwordTextField.fill(excel_data[4][1], timeout=60000)

    def clickOnContinueBtn(self):
        self.continueBtn.click(timeout=60000)              

    def validateNextSignPage(self):
        # Verify that the next sign-in step is displayed
        expect(self.passwordTextField).to_be_visible(timeout=60000)  # Adjust the timeout as needed
    