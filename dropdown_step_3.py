from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    number_one = browser.find_element(By.XPATH, '//span[@class="nowrap"][@id="num1"]').text
    number_two = browser.find_element(By.XPATH, '//span[@class="nowrap"][@id="num2"]').text
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(int(number_one) + int(number_two)))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


finally:
    time.sleep(30)
    browser.quit()
