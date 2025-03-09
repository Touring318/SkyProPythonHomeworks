# Task2 - Calc

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_sum():

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.implicitly_wait(4)
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )
    # В поле ввода по локатору #delay ввести значение 45
    driver.find_element(By.CSS_SELECTOR, 'input#delay').clear()
    driver.find_element(By.CSS_SELECTOR, 'input#delay').send_keys('45')
    # Сложить 7+8
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    waiter = WebDriverWait(driver, 48)
    # Ждать пока не появится результат
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
    )
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    # print(result)
    assert int(result) == 15
    driver.quit()
