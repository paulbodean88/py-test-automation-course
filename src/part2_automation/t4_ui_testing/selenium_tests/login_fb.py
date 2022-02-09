import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Step 1) Open Firefox
driver = webdriver.Chrome('/Users/paulb/Documents/GitHub/py-test-automation-course/resources/chromedriver')
# Step 2) Navigate to Facebook
driver.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
time.sleep(2)
Alert(driver).accept()
# driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, '#u_0_j_0\+'))

time.sleep(2)
username = driver.find_element(By.CSS_SELECTOR, "#email")
password = driver.find_element(By.CSS_SELECTOR, "#pass")
submit = driver.find_element(By.CSS_SELECTOR, '#u_0_d_sP')
username.send_keys("you@email.com")
password.send_keys("yourpassword")
# Step 4) Click Login
submit.click()
