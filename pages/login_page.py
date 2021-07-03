from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        is_correct_url = "login" in self.current_url
        assert is_correct_url, "The current url is incorrect."

    def should_be_login_form(self):
        is_login_form_exists = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM),
            'Error find login form.')
        assert is_login_form_exists, 'Error find login form.'

    def should_be_register_form(self):
        is_register_form_exists = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.REGISTER_FORM),
            'Error find register form.')
        assert is_register_form_exists, 'Error find register form.'
