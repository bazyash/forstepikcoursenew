from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Login page is not opened'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        self.go_to_login_page()
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REG_INPUT)
        email_input.send_keys(email)
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REG_INPUT)
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REG_CONFIRM_INPUT)
        password2_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
