from selenium.webdriver.common.by import By

from src.part2_automation.t4_ui_testing.pom_demo_auto.pages.base import BasePage


class AutocompleteLocators:
    ADR = (By.ID, 'autocomplete')
    STR_1 = (By.ID, 'street_number')
    STR_2 = (By.ID, 'route')
    CITY = (By.ID, 'locality')
    STATE = (By.ID, 'administrative_area_level_1')
    ZIP = (By.ID, 'postal_code')
    COUNTRY = (By.ID, 'country')


class Autocomplete(BasePage):
    def title_page(self):
        return self.driver.title

    def find_elem_wrapper(self, locator, test_data):
        self.driver.find_element(*locator).send_keys(test_data)

    def enter_adr(self, value):
        print(f'Click on  {AutocompleteLocators.ADR} and search for {value}')
        # self.driver.find_element(*AutocompleteLocators.ADR).send_keys(value)
        self.find_elem_wrapper(AutocompleteLocators.ADR, value)

    def enter_str1(self, value):
        print(f'Click on  {AutocompleteLocators.STR_1} and search for {value}')
        self.find_elem_wrapper(AutocompleteLocators.STR_1, value)

    def enter_str2(self, value):
        print(f'Click on  {AutocompleteLocators.STR_2} and search for {value}')
        self.find_elem_wrapper(AutocompleteLocators.STR_2, value)

    def enter_city(self, value):
        print(f'Click on  {AutocompleteLocators.CITY} and search for {value}')
        self.find_elem_wrapper(AutocompleteLocators.CITY, value)

    def enter_state(self, value):
        print(f'Click on  {AutocompleteLocators.STATE} and search for {value}')
        self.find_elem_wrapper(AutocompleteLocators.STATE, value)

    def enter_zip(self, value):
        print(f'Click on  {AutocompleteLocators.ZIP} and search for {value}')
        self.find_elem_wrapper(AutocompleteLocators.ZIP, value)

    def enter_country(self, value):
        print(f'Click on  {AutocompleteLocators.COUNTRY} and search for {value}')
        self.find_elem_wrapper(AutocompleteLocators.COUNTRY, value)

