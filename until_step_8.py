from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    element = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id='price']"), '100'))
    button = browser.find_element(By.CSS_SELECTOR, '[id="book"]')
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    print(browser.switch_to.alert.text.split()[-1])


finally:
    time.sleep(5)
    browser.quit()
