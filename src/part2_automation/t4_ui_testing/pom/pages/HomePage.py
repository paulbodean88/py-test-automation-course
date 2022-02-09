import time

from src.part2_automation.t4_ui_testing.pom.locators.HomeLocators import HomeLocators


class HomePage:
    def __init__(self, driver):
        self._driver = driver
        self._search = HomeLocators.SEARCH_FIELD
        self._search_btn = HomeLocators.SEARCH_BTN
        self._direction = HomeLocators.DIRECTION_BTN
        self._search_result = HomeLocators.SEARCH_RESULT_LST
        self._search_items = HomeLocators.SEARCH_LIST

    def query_adr(self, address):
        self._driver.find_element(*self._search).send_keys(address)
        time.sleep(1.0)

    def click_search(self):
        self._driver.find_element(*self._search_btn).click()

    def click_direction(self):
        self._driver.find_element(*self._direction).click()
        time.sleep(1.0)

    def get_list(self):
        result = self._driver.find_element(*self._search_result)
        return [x.text for x in result.find_elements(*self._search_items)]
