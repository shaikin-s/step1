import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.smoke
@pytest.mark.parametrize('number_of_lesson', ['895', '896', '897', '898', '899', '903', '904', '905'])
def test_stepik_page(browser, number_of_lesson):
    link = f"https://stepik.org/lesson/236{number_of_lesson}/step/1"
    browser.get(link)
    browser.implicitly_wait(20)
    browser.find_element(By.XPATH, '//a[contains(@href,"login")]').click()
    browser.find_element(By.XPATH, '//input[contains(@autocomplete,"email")]').send_keys('sergeishaikin6@gmail.com')
    browser.find_element(By.XPATH, '//input[contains(@autocomplete,"password")]').send_keys('Qwertyu1!')
    browser.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    answer = str(math.log(int(time.time())))
    browser.implicitly_wait(20)
    browser.find_element(By.XPATH, '//textarea').send_keys(answer)
    browser.implicitly_wait(20)
    button_submit = browser.find_element(By.XPATH, '//button[contains(@class,"submit")]')
    browser.implicitly_wait(5)
    button_submit.click()
    browser.implicitly_wait(20)
    message = browser.find_element(By.XPATH, '//p[contains(@class,"smart")]')
    assert "Correct!" in message.text
