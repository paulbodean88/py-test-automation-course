import time

import pytest
from selenium.webdriver.common.by import By

from src.part2_automation.t4_ui_testing.pom.Base import Base
from src.part2_automation.t4_ui_testing.pom.pages.HomePage import HomePage


@pytest.mark.usefixtures('set_up')
class TestOSMHome(Base):
    def test_search(self):
        print('Test started')
        driver = self.driver
        home = HomePage(driver)
        home.query_adr('Cluj-Napoca')
        time.sleep(2)
        home.click_search()
        time.sleep(2)
        # home.click_direction()
        result = home.get_list()
        print(result)
