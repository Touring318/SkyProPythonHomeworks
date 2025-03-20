# Task1 - data_types_form

# import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.color import Color

from pages.data_types_form import data_types

# шестнадцатеричный код красного цвета
bg_color_red = '#F8D7DA'
# шестнадцатеричный код зеленого цвета
bg_color_green = '#D1E7DD'
url = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'


def test_data_types_form():

    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    form = data_types(browser)
    form.open(url)
    form.fill_out_a_form()
    # Проверить цвет фона полей ввода
    for i in range(10):
        if i != 3:
            hex_color = form.color_in_hex(form.get_input_fields(), i)
            assert bg_color_green == str(hex_color), \
                f'цвет фона {i}-поля не зеленый'
        else:
            hex_color = form.color_in_hex(form.get_input_fields(), i)
            assert bg_color_red == str(hex_color), \
                f'цвет фона {i}-поля не красный'
    form.close_browser()
