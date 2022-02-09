from selenium.webdriver.common.by import By


class HomeLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, '#sidebar #query')
    SEARCH_BTN = (By.CSS_SELECTOR, '#sidebar .col .btn')
    DIRECTION_BTN = (
        By.CSS_SELECTOR, '#sidebar > div.search_forms > form.search_form.px-1.py-2 > div > div.col-auto > a > img')
    SEARCH_RESULT_LST = (By.XPATH, '//*[@id="sidebar_content"]/div[2]/ul')
    SEARCH_LIST = (By.TAG_NAME, 'li')
