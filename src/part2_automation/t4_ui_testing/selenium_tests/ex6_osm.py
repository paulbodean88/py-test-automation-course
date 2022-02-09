import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.openstreetmap.org/#map=7/45.997/24.983')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#sidebar #query').send_keys('Cluj')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#sidebar .col .btn').click()
time.sleep(5)
txt = driver.find_element(By.CSS_SELECTOR, "#sidebar_content > div:nth-child(3) > ul > li:nth-child(1) > a").text
print(txt)
