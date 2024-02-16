import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    link = 'http://selenium1py.pythonanywhere.com/'
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, 'button.btn')
            pytest.fail('Should not be button Send')
    finally:
        browser.quit()


def test_exception2():
    link = 'http://selenium1py.pythonanywhere.com/'
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, 'submit_button.btn')
            pytest.fail('Should not be button Send')
    finally:
        browser.quit()
