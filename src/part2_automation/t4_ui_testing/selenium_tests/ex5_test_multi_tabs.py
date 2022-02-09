import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# locators definition
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

click = (By.CSS_SELECTOR, '#content > div > a')


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(*click).click()
time.sleep(2.0)

one = driver.window_handles[0]
two = driver.window_handles[1]
time.sleep(1)
i = 0
while i < 10:
    driver.switch_to.window(one)
    driver.switch_to.window(two)
    i += 1

driver.quit()
