from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_login-password')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REG_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_REG_CONFIRM_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERTS = (By.CSS_SELECTOR, '.alertinner')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"]')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')
    PRODUCTS_BLOCK = (By.XPATH, '.basket-items')