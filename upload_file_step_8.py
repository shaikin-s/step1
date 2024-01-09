import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first_name.send_keys('Tom')
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name.send_keys('Smith')
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('tom@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'test.txt'
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(1)
    browser.quit()

