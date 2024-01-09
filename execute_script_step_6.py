import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    value_x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    x = calc(value_x)
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(x)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    radiobutton.click()
    button.click()
    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(30)
    browser.quit()
