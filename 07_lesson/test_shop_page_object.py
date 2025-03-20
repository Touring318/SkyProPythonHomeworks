from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.shop_mainpage import Mainpage
from pages.shop_cart_page import Cart
from pages.shop_checkout_step1_page import CheckoutStepOne
from pages.shop_checkout_step2_page import CheckoutStepTwo


shop_logon_page_url = 'https://www.saucedemo.com/'
shop_cart_url = 'https://www.saucedemo.com/cart.html'
shop_checkout_step_one_url = 'https://www.saucedemo.com/checkout-step-one.html'
shop_checkout_step_two_url = 'https://www.saucedemo.com/checkout-step-two.html'


def test_shop():

    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    mainpage = Mainpage(browser)
    mainpage.open(shop_logon_page_url)
    mainpage.fill_out_logon_page_and_login()
    mainpage.add_items_to_cart()

    cartpage = Cart(browser)
    cartpage.open(shop_cart_url)
    cartpage.press_checkout_button()

    checkout_step1 = CheckoutStepOne(browser)
    checkout_step1.open(shop_checkout_step_one_url)
    checkout_step1.fill_out_and_submit_data()

    checkout_step2 = CheckoutStepTwo(browser)
    checkout_step2.open(shop_checkout_step_two_url)
    summary_total = checkout_step2.get_summary_total()
    browser.quit()
    assert summary_total == 'Total: $58.29', \
        'Итоговая сумма не равна сумме цен товаров'
