import sys
import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.part2_automation.t4_ui_testing.pom_demo_auto.pages.autocomplete_page import Autocomplete
from src.part2_automation.t4_ui_testing.pom_demo_auto.pages.home_page import HomePage


class TestQueryAutocomplete(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://formy-project.herokuapp.com/")

    def test_query(self):
        main = HomePage(self.driver)
        main.click_on_components()
        auto_page = Autocomplete(self.driver)

        self.assertEqual(auto_page.title_page(), 'Formy')
        auto_page.enter_adr('Iasi')
        time.sleep(1)
        auto_page.enter_str1('Calea Clujului')
        time.sleep(1)
        auto_page.enter_str2('Popesti')
        time.sleep(1)
        auto_page.enter_city('Dej')
        time.sleep(1)
        auto_page.enter_state('Iasi')
        time.sleep(1)
        auto_page.enter_zip(400117)
        time.sleep(1)
        auto_page.enter_country('Russia')

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



