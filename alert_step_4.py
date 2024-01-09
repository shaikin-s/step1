from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_blue = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_blue.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    value = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    value_number = value.text
    y = calc(value_number)
    answer = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    answer.send_keys(y)
    button_confirm = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_confirm.click()
    print(browser.switch_to.alert.text.split()[-1])


finally:
    time.sleep(5)
    browser.quit()
