import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class MapGestures:
    def __init__(self, driver):
        self._driver = driver

    def zoom_in(self):
        time.sleep(2.0)
        # self._driver.find_element(By.ID('map')).

