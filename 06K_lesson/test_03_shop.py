# Task3 - Shop

def test_03_shop():

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(5)
    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie').click()
    driver.get('https://www.saucedemo.com/cart.html')

    driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()
    driver.get('https://www.saucedemo.com/checkout-step-one.html')

    driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('Василий')
    driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys('Пупкин')
    driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys('554433')
    driver.find_element(By.CSS_SELECTOR, 'input#continue').click()
    driver.get('https://www.saucedemo.com/checkout-step-two.html')

    # w_handles = driver.window_handles
    # print(len(w_handles))
    # print(w_handles)

    summary_total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
    driver.quit()
    print(summary_total)
    assert summary_total == 'Total: $58.29', f'Итоговая сумма не равна сумме цен товаров'
