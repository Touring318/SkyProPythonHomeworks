# Task1 - Form

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


def test_01_form_submission():

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
    )
    # Находим и заполняем поле First name
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')\
        .send_keys('Иван')
    # Находим и заполняем поле Last name
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')\
        .send_keys('Петров')
    # Находим и заполняем поле Address
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')\
        .send_keys('Ленина, 55-3')
    # Находим и заполняем поле Email
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')\
        .send_keys('test@skypro.com')
    # Находим и заполняем поле Phone number
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')\
        .send_keys('+7985899998787')
    # Находим и заполняем поле City
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')\
        .send_keys('Москва')
    # Находим и заполняем поле Country
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')\
        .send_keys('Россия')
    # Находим и заполняем поле Job position
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')\
        .send_keys('QA')
    # Находим и заполняем поле Company
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')\
        .send_keys('SkyPro')
    # Находим и нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    # Ждем обновления статуса полей ввода
    driver.implicitly_wait(5)
    # Собираем идентификаторы полей ввода данных
    input_fields = driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2')
    # Проверка количества собранных значений
    # print(len(input_fields))
    # Просмотреть собранные значения
    # for i in range(10):
    #     print(input_fields[i])

    # шестнадцатеричный код красного цвета
    bg_color_red = '#F8D7DA'
    # шестнадцатеричный код зеленого цвета
    bg_color_green = '#D1E7DD'

    # Проверить цвет фона полей ввода
    for i in range(10):
        if i != 3:
            back_color = input_fields[i]\
                .value_of_css_property("background-color")
            color_in_hex = Color.from_string(back_color).hex.upper()
            # для самопроверки можно вывести полученное из атрибута значение\
            # "background-color"(RGBA), этот же цвет в HEX-виде и имя поля
            # id__ = input_fields[i].get_attribute('id')
            # print(back_color, color_in_hex, id__)
            assert bg_color_green == str(color_in_hex), \
                   f'цвет фона {i}-поля не зеленый'
        else:
            back_color = input_fields[i]\
                .value_of_css_property("background-color")
            color_in_hex = Color.from_string(back_color).hex.upper()
            # id__ = input_fields[i].get_attribute('id')
            # # print(back_color, color_in_hex, id__)
            assert bg_color_red == str(color_in_hex), \
                   f'цвет фона {i}-поля не красный'
    driver.quit()
