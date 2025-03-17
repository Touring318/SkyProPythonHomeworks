from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):
        self._driver = driver

    def open(self, shop_cart_url):
        self._driver.implicitly_wait(4)
        self._driver.get(shop_cart_url)
        # self._driver.maximize_window()

    def press_checkout_button(self):
        # Нажать кнопку "Checkout"
        self._driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()
