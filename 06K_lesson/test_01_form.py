# Task1 - Form
# import pytest

def test_01_form_submission():

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.color import Color

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    # Находим и заполняем поле First name
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys('Иван')
    # Находим и заполняем поле Last name
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys('Петров')
    # Находим и заполняем поле Address
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys('Ленина, 55-3')
    # Находим и заполняем поле Email
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys('test@skypro.com')
    # Находим и заполняем поле Phone number
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys('+7985899998787')
    # Находим и заполняем поле City
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys('Москва')
    # Находим и заполняем поле Country
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys('Россия')
    # Находим и заполняем поле Job position
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys('QA')
    # Находим и заполняем поле Company
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys('SkyPro')
    # Находим и нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    # Ждем обновления статуса полей ввода
    driver.implicitly_wait(5)
    # Собираем идентификаторы полей ввода данных
    inputFields = driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2')
    # Проверка количества собранных значений
    # print(len(inputFields))
    # Просмотреть собранные значения
    # for i in range(10):
    #     print(inputFields[i])

    bgColorRed = '#F8D7DA'          # шестнадцатеричный код красного цвета
    bgColorGreen = '#D1E7DD'        # шестнадцатеричный код зеленого цвета

    # Проверить цвет фона полей ввода
    for i in range(10):
        if i != 3:
            backColor = inputFields[i].value_of_css_property("background-color")
            colorInHEX = Color.from_string(backColor).hex.upper()
            # для самопроверки можно вывести полученное из атрибута значение 
            # "background-color"(RGBA), этот же цвет в HEX-виде и имя поля
            # id__ = inputFields[i].get_attribute('id')
            # print(backColor, colorInHEX, id__)
            assert bgColorGreen == str(colorInHEX), f'цвет фона {i}-поля не зеленый'
        else:
            backColor = inputFields[i].value_of_css_property("background-color")
            colorInHEX = Color.from_string(backColor).hex.upper()
            # id__ = inputFields[i].get_attribute('id')
            # # print(backColor, colorInHEX, id__)
            assert bgColorRed == str(colorInHEX), f'цвет фона {i}-поля не красный'
    driver.quit()
