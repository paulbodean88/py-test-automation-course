import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/paulb/Documents/GitHub/py-test-automation-course/resources/chromedriver')

driver.get("https://www.google.com")
time.sleep(1)
driver.maximize_window()
driver.find_element(By.ID, 'L2AGLb').click()
search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys('sheriff tiraspol!')

search_bar.submit()
time.sleep(3.0)
driver.refresh()

time.sleep(3.0)
driver.quit()
