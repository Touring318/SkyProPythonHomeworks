from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.calc_page import Calculator

url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
delay = 45


def test_calculator_page():

    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    calculator_page = Calculator(browser)
    calculator_page.open(url)
    calculator_page.introduce_a_delay(delay)
    result = calculator_page.perform_addition()
    assert int(result) == 15
    calculator_page.close_browser()
