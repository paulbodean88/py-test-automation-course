import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


# locators definition
from webdriver_manager.chrome import ChromeDriverManager


class TestAuth(unittest.TestCase):
    auth_btn = (By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')

    def test_auth(self):
        self.driver.find_element(*self.auth_btn).click()
        username = 'admin'
        password = 'admin'
        time.sleep(1)
        self.driver.get('https://' + username + ':' + password + '@' + 'the-internet.herokuapp.com/basic_auth')

        print(self.driver.title)
        # self.assertEquals()
        time.sleep(1)
        self.driver.back()
        self.driver.back()

    def tearDown(self) -> None:
        self.driver.quit()
