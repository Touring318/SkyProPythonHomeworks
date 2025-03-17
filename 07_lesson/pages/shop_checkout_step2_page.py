from selenium.webdriver.common.by import By


class CheckoutStepTwo:

    def __init__(self, driver):
        self._driver = driver

    def open(self, shop_checkout_step_two_url):
        self._driver.implicitly_wait(4)
        self._driver.get(shop_checkout_step_two_url)
        # self._driver.maximize_window()

    def get_summary_total(self):
        summary_total = self._driver.find_element(
            By.CSS_SELECTOR, 'div.summary_total_label').text
        return summary_total
