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
