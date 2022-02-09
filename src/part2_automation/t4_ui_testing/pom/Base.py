import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        print('Install Chrome driver')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.openstreetmap.org/#map=7/46.001/24.983')
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
