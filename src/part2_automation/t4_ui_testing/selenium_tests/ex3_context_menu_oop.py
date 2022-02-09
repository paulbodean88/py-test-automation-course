import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestContext(unittest.TestCase):
    # locators definition
    box = (By.ID, 'hot-spot')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/context_menu")

    def test_context(self):
        actionChains = ActionChains(self.driver)
        actionChains.context_click(self.driver.find_element(*self.box)).perform()
        time.sleep(1)
        self.driver.switch_to.alert.accept()

        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()
