import time

from selenium.webdriver.common.by import By

from src.part2_automation.t4_ui_testing.pom_demo_auto.pages.base import BasePage


class HomePage(BasePage):
    COMPONENTS = (By.LINK_TEXT, 'Autocomplete')
    BUTTONS = (By.LINK_TEXT, 'TBA')
    CHECKBOX = (By.LINK_TEXT, 'TBA')

    def click_on_components(self):
        print(f'Click on {self.COMPONENTS}')
        time.sleep(3)
        self.driver.find_element(*self.COMPONENTS).click()

    def click_on_buttons(self):
        print(f'Click on {self.BUTTONS}')

    def click_on_checkbox(self):
        print(f'Click on {self.CHECKBOX}')
