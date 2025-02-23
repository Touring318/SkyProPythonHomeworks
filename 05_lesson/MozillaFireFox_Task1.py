# FireFox Task1 - Modal window

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(5)

# Закрываем Modal Window
# Ниже Два варианта закрытия модального окна, один из которых закомментирован:

driver.find_element(By.CSS_SELECTOR, '.modal-footer').click()
# driver.find_element(By.XPATH, '//p[text()="Close"]').click()
