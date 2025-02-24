# FireFox Task3 - Authorization Form

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys - не потребовалось

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/login')
sleep(5)
usernameInput = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
passwordInput = driver.find_element(By.CSS_SELECTOR, 'input#password')

# Username Input
usernameInput.send_keys("tomsmith")
# Password Input
passwordInput.send_keys("SuperSecretPassword!")
# Submit LoginCredentials
driver.find_element(By.CSS_SELECTOR, 'i.fa.fa-2x.fa-sign-in').click()
