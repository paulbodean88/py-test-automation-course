import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.part2_automation.t4_ui_testing.pom.Base import Base
from src.part2_automation.t4_ui_testing.pom.pages.MapGesturesPage import MapGestures


@pytest.mark.usefixtures('set_up')
class TestOSMHome(Base):
    def test_map(self):
        print('Test started')
        driver = self.driver
        # map = MapGestures(driver)
        # map.zoom_in()
        action = ActionChains(driver)
        action.double_click(driver.find_element(By.ID, 'map'))
        time.sleep(2)
        action.double_click(driver.find_element(By.ID, 'map'))
        time.sleep(2)
        action.double_click(driver.find_element(By.CSS_SELECTOR, '#map'))
        time.sleep(2)