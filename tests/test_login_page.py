import pytest
import time
from pages.login_page import LoginPage

class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)

    @pytest.mark.parametrize('login, password', [('test','test'), ('test1','test1'), ('test2','tes2t')])
    def test_login_in_account(self, login, password):
        self.login_page.open()
        self.login_page.enter_login(login)
        self.login_page.enter_password(password)
        self.login_page.click_submit_button()
        time.sleep(1)
        assert self.login_page.error_validation, "Нет ошибки валидации поля email"