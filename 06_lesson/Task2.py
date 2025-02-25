# Task2 - Button rename

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver,5)

driver.get('http://uitestingplayground.com/textinput')
newOnButtonText = 'SkyPro'

inputForm = driver.find_element(By.CSS_SELECTOR, 'input#newButtonName')
inputForm.send_keys(newOnButtonText)

driver.find_element(By.CSS_SELECTOR, 'button#updatingButton').click()
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button#updatingButton'), newOnButtonText)
)
text = driver.find_element(By.CSS_SELECTOR, 'button#updatingButton').text
print(text)

driver.quit()
