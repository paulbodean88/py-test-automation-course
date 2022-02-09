import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.diemol.com/selenium-4-demo/relative-locators-demo.html')

element = driver.find_elements(locate_with(By.TAG_NAME, "li")
                               .to_left_of({By.ID: "berlin"})
                               .below({By.ID: "warsaw"}))[0]

time.sleep(2.0)
driver.execute_script("arguments[0].style.filter='blur(8px)'", element)
time.sleep(3.0)

assert element.get_attribute('id') == 'london'

driver.execute_script("document.getElementById('movember').click();")
time.sleep(2)
