import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    user = (By.ID, 'username')
    pwd = (By.ID, 'password')
    login = (By.CLASS_NAME, 'radius')
    msg = (By.CLASS_NAME, 'subheader')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('/Users/paulb/Documents/GitHub/py-test-automation-course/resources/chromedriver')
        self.driver.get("https://the-internet.herokuapp.com/login")

    def test_invalid_login(self):
        self.driver.find_element(*self.user).send_keys('test@gmail.com')
        time.sleep(1)
        self.driver.find_element(*self.pwd).send_keys('abc')
        time.sleep(1)
        self.driver.find_element(*self.login).click()
        time.sleep(1)

    def test_valid_login(self):
        self.driver.find_element(*self.user).send_keys('tomsmith')
        time.sleep(1)
        self.driver.find_element(*self.pwd).send_keys('SuperSecretPassword!')
        time.sleep(1)
        self.driver.find_element(*self.login).click()
        time.sleep(1)

    def test_logout(self):
        self.test_valid_login()
        logout = (By.CSS_SELECTOR, '#content > div > a > i')
        self.driver.find_element(*logout).click()
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    test = TestLogin()
    test.test_invalid_login()
