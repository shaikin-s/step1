import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestLinks(unittest.TestCase):
    def test_link1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'

        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys('Ivan')
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys('Petrov')
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys('shaikin@gmail.com')
        input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input4.send_keys('12345678901')
        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys('Russia')
        button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button.click()
        text_actual = browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(text_actual, "Congratulations! You have successfully registered!", "Text should be the same")

    def test_link2(self):
        link2 = 'http://suninjuly.github.io/registration2.html'

        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys('Ivan')
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys('Petrov')
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys('shaikin@gmail.com')
        input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input4.send_keys('12345678901')
        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys('Russia')
        button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button.click()
        text_actual = browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(text_actual, "Congratulations! You have successfully registered!", "Text should be the same")


if __name__ == "__main__":
    unittest.main()
