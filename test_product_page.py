import pytest

import time

from pages.product_page import ProductPage
from pages.login_page import LoginPage


@pytest.mark.parametrize('promo', ["/?promo=offer0",
                                   "/?promo=offer1",
                                   "/?promo=offer2",
                                   "/?promo=offer3",
                                   "/?promo=offer4",
                                   "/?promo=offer5",
                                   "/?promo=offer6",
                                   pytest.param(
                                       "/?promo=offer7", marks=pytest.mark.xfail),
                                   "/?promo=offer8",
                                   "/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_is_correct()
    page.product_price_is_correct()
    page.check_message_about_adding_to_basket()

@pytest.mark.xfail(reason="Test should fall because guest can see success message after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Test should fall because success message is not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_dissapear_of_success_message()
