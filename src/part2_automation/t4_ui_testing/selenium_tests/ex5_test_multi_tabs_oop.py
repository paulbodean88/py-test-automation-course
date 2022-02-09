import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

# locators definition
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestMultiTabs(unittest.TestCase):
    CLICK = (By.CSS_SELECTOR, '#content > div > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/windows')

    def test_switch_tabs(self):
        self.driver.find_element(*self.CLICK).click()
        time.sleep(2.0)
        # WebDriverWait(self.driver, 5).until(EC.number_of_windows_to_be(2))
        one = self.driver.window_handles[0]
        two = self.driver.window_handles[1]
        time.sleep(1)
        i = 0
        while i < 15:
            self.driver.switch_to.window(one)
            self.driver.switch_to.window(two)
            i += 1

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
