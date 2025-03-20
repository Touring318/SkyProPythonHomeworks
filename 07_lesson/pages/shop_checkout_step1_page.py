from selenium.webdriver.common.by import By


class CheckoutStepOne:

    def __init__(self, driver):
        self._driver = driver

    def open(self, shop_checkout_step_one_url):
        self._driver.implicitly_wait(4)
        self._driver.get(shop_checkout_step_one_url)
        # self._driver.maximize_window()

    def fill_out_and_submit_data(self):
        self._driver.find_element(By.CSS_SELECTOR, 'input#first-name')\
            .send_keys('Василий')
        self._driver.find_element(By.CSS_SELECTOR, 'input#last-name')\
            .send_keys('Пупкин')
        self._driver.find_element(By.CSS_SELECTOR, 'input#postal-code')\
            .send_keys('554433')
        self._driver.find_element(By.CSS_SELECTOR, 'input#continue')\
            .click()
