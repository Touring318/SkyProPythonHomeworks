# Task3 - Picture wait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver,20)

# Переходим по ссылке
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

# Ждем пока не появится надпись Done! (Загрузка изображений окончена)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p#text.lead'), 'Done!')
)
# Находим контейнер с изображениями
div = driver.find_element(By.CSS_SELECTOR, 'div#image-container')
# Собираем идентификаторы изображений в контейнере
sources = div.find_elements(By.CSS_SELECTOR, 'img')
# Получаем значение атрибута src для третьей картинки
source = sources[2].get_attribute('src')
# Выводим полученное значение в консоль
print(source)
driver.quit()
