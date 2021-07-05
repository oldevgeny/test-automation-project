from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn.btn-default")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner h2")


class MainPageLocators(BasePageLocators):
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (
        By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info p strong")
    PRODUCT_PRICE_IN_STORE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")
