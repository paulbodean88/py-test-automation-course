from selenium import webdriver

if __name__ == "__main__":
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--headless')
    chrome_opt.add_argument('--no-sandbox')

    driver = webdriver.Chrome('./chromedriver', options=chrome_opt)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    print(driver.title)
    driver.close()
