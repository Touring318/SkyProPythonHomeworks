# FireFox Task2 - Input Field

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/inputs')
sleep(2)
numberInputField = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
numberInputField.send_keys("1", "0", "0", "0")
sleep(2)
numberInputField.clear()
numberInputField.send_keys("999")
