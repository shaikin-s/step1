import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_for_click = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_for_click.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    value_x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = value_x.text
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    answer.send_keys(y)
    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_submit.click()
    print(browser.switch_to.alert.text.split()[-1])
    print(browser.switch_to.alert.text.split()[0])
    print(browser.switch_to.alert.text.split()[-2])

finally:
    time.sleep(5)
    browser.quit()
