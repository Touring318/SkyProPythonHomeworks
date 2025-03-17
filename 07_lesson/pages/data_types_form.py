from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


class data_types:

    def __init__(self, driver):
        self._driver = driver

    def open(self, url):
        # открыть форму по ссылке
        self._driver.get(url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_out_a_form(self):
        # Находим и заполняем поля формы
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')\
            .send_keys('Иван')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')\
            .send_keys('Петров')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')\
            .send_keys('Ленина, 55-3')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')\
            .send_keys('test@skypro.com')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')\
            .send_keys('+7985899998787')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')\
            .send_keys('Москва')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')\
            .send_keys('Россия')
        self._driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]').send_keys('QA')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')\
            .send_keys('SkyPro')
        # Находим и нажимаем кнопку Submit
        self._driver.find_element(
            By.CSS_SELECTOR, 'button[type=submit]').click()

    def color_in_hex(self, input_fields, i):
        back_color = input_fields[i]\
               .value_of_css_property("background-color")
        color_in_hex = Color.from_string(back_color).hex.upper()
        return color_in_hex

    def get_input_fields(self):
        # Собираем идентификаторы полей ввода данных
        input_fields = self._driver.find_elements(
            By.CSS_SELECTOR, 'div.alert.py-2')
        return input_fields

    def close_browser(self):
        # Закрыть браузер
        self._driver.quit()
