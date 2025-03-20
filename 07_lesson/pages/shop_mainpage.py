from selenium.webdriver.common.by import By


class Mainpage:

    def __init__(self, driver):
        self._driver = driver

    def open(self, shop_logon_page_url):
        self._driver.implicitly_wait(4)
        self._driver.get(shop_logon_page_url)
        self._driver.maximize_window()

    def fill_out_logon_page_and_login(self):
        self._driver.find_element(By.CSS_SELECTOR, 'input#user-name')\
            .send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, 'input#password')\
            .send_keys('secret_sauce')
        self._driver.find_element(
            By.CSS_SELECTOR, 'input#login-button').click()
        self._driver.maximize_window()

    def add_items_to_cart(self):
        self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt')\
            .click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie').click()
