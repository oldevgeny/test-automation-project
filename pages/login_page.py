from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        is_correct_url = "login" in self.browser.current_url
        assert is_correct_url, "The current url is incorrect."

    def should_be_login_form(self):
        is_login_form_exists = self.is_element_present(
            *LoginPageLocators.LOGIN_FORM)
        assert is_login_form_exists, 'Error find login form.'

    def should_be_register_form(self):
        is_register_form_exists = self.is_element_present(
            *LoginPageLocators.REGISTER_FORM)
        assert is_register_form_exists, 'Error find register form.'
