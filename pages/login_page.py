from pages.base_page import BasePage

class LoginPage(BasePage):

    PAGE_URL = "https://www.freeconferencecall.com/global/login"
    EMAIL_INPUT_LOCATOR = ('id', 'login_email')
    PASSWORD_INPUT_LOCATOR = ('id', 'password')
    LOGIN_SUBMIT_LOCATOR = ('id', 'loginformsubmit')
    ERROR_EMAIL_LOCATOR = ('xpath', '//li[text()="This value should be a valid email"]')
    def enter_login(self, email):
        login_input = self.driver.find_element(*self.EMAIL_INPUT_LOCATOR)
        login_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR)
        password_input.send_keys(password)

    def click_submit_button(self):
        self.click_on_element(self.LOGIN_SUBMIT_LOCATOR)

    def error_validation(self):
        self.element_is_present(self.ERROR_EMAIL_LOCATOR)