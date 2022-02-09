import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# locators definition
user = (By.ID, 'username')
pwd = (By.ID, 'password')
login = (By.CLASS_NAME, 'radius')
msg = (By.CLASS_NAME, 'subheader')

# driver init
driver = webdriver.Chrome('/Users/paulb/Documents/GitHub/py-test-automation-course/resources/chromedriver')
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
print('Start test 1 for an invalid login')
driver.find_element(*user).send_keys('test@gmail.com')
time.sleep(1)
driver.find_element(*pwd).send_keys('abc')
time.sleep(1)
driver.find_element(*login).click()
time.sleep(1)

print('Start test 2 for an valid login')
driver.find_element(*user).send_keys('tomsmith')
time.sleep(1)
driver.find_element(*pwd).send_keys('SuperSecretPassword!')
time.sleep(1)
driver.find_element(*login).click()
time.sleep(1)

print('Start test 3 to logout')
logout = (By.CSS_SELECTOR, '#content > div > a > i')
driver.find_element(*logout).click()
time.sleep(1)

print('Start test 4 to login with dynamically collected usr and pwd')
# get usr and pwd from the sub-header, and login again
content = driver.find_element(*msg).text

lst = content.split('.')[1].split()

# lst = ['Enter', 'tomsmith', 'for', 'the', 'username', 'and', 'SuperSecretPassword!', 'for', 'the', 'password']
dynamic_usr, dynamic_pwd = 'na', 'na'

for i in range(0, len(lst)):
    if lst[i] == 'Enter':
        dynamic_usr = lst[i + 1]
    if lst[i] == 'and':
        dynamic_pwd = lst[i + 1]
x = [lst[i + 1] for i in range(0, len(lst)) if lst[i] == 'Enter']

print(f'user {dynamic_usr} and pwd {dynamic_pwd}')

driver.find_element(*user).send_keys(dynamic_usr)
time.sleep(1)
driver.find_element(*pwd).send_keys(dynamic_pwd)
time.sleep(1)
driver.find_element(*login).click()
time.sleep(1)
driver.quit()
