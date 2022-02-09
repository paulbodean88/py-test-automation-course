import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_context():
    # locators definition
    box = (By.ID, 'hot-spot')

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://the-internet.herokuapp.com/context_menu")

    actionChains = ActionChains(driver)

    actionChains.context_click(driver.find_element(*box)).perform()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.quit()

# to run use: pytest ex3_context_menu_fun.py