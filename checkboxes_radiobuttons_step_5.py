import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//span[@class='nowrap'][@id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)
    checkbox = browser.find_element(By.XPATH, "//input[@class='form-check-input'][@type='checkbox']")
    checkbox.click()
    radio = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
