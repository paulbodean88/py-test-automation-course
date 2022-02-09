import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# locators definition
box = (By.ID, 'hot-spot')

# driver init
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/context_menu")
action = ActionChains(driver)

action.context_click(driver.find_element(*box)).perform()

time.sleep(1)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()

time.sleep(1)

driver.quit()
