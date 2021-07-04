from pages.product_page import ProductPage
from pages.login_page import LoginPage

import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_is_correct()
    page.product_price_is_correct()
    page.check_message_about_adding_to_basket()
