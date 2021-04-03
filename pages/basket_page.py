from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_BLOCK), 'Products are presented, but should not be'
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE)
        message_text = empty_basket_message.text
        assert 'Your basket is empty' in message_text, 'Empty basket message is not presentd'


    def should_be_alerts(self):
        product_name = self.get_product_name()
        product_price = self.get_price()
        alert_banners = self.browser.find_elements(*ProductPageLocators.ALERTS)
        alert_texts = []
        for alert in alert_banners:
            alert = alert.text
            if '\n' in alert:
                alert = alert.split('\n')[0]
            alert_texts.append(alert)
        expected_alert_1 = product_name + ' has been added to your basket.'
        expected_alert_2 = 'Your basket total is now ' + str(product_price)
        assert expected_alert_1 in alert_texts, f'{expected_alert_1} is not in {alert_texts}'
        assert expected_alert_2 in alert_texts, f'{expected_alert_2} is not in {alert_texts}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message was not dissappeared, but should be"

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