import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# locators definition
from webdriver_manager.chrome import ChromeDriverManager

auth_btn = (By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a')

# driver init
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://the-internet.herokuapp.com/')
driver.find_element(*auth_btn).click()
username = 'admin'
password = 'admin'
time.sleep(1)
driver.get('https://' + username + ':' + password + '@the-internet.herokuapp.com/basic_auth')

print(driver.title)
time.sleep(1)
driver.back()
driver.back()
