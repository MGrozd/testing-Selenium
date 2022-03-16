import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

with webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())) as driver:
    driver.implicitly_wait(2)
    driver.delete_all_cookies()
    driver.get('https://login.yahoo.com/')
    assert 'Yahoo' in driver.title
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@id='login-username']").send_keys('edureka@yahoo.com')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='login-signin']").click()
    time.sleep(3)
    assert 'No results found.' not in driver.page_source

