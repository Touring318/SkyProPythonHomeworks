from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self._driver = driver

    def open(self, url):
        # открыть форму по ссылке
        self._driver.get(url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def introduce_a_delay(self, delay):
        # В поле ввода по локатору #delay ввести значение delay
        self._driver.find_element(By.CSS_SELECTOR, 'input#delay').clear()
        self._driver.find_element(
            By.CSS_SELECTOR, 'input#delay').send_keys(delay)

    def perform_addition(self):
        # Сложить 7+8
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
        waiter = WebDriverWait(self._driver, 48)
        # Ждать пока не появится результат
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), '15')
        )
        result = self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        return result

    def close_browser(self):
        # Закрыть браузер
        self._driver.quit()
