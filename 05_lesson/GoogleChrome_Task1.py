# Chrome Task 1 -Button Click

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

addButton = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
addButton.click()
addButton.click()
addButton.click()
addButton.click()
addButton.click()

search_field = "button.added-manually"
deleteButtons = driver.find_elements(By.CSS_SELECTOR, search_field)
print(len(deleteButtons))

sleep(3)
