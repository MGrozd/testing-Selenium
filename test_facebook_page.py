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
    driver.get('https://hr-hr.facebook.com/r.php?locale=hr_HR&display=page')
    assert 'Facebook' in driver.title
    driver.maximize_window()
    day_select_elem = driver.find_element(By.ID, 'day')
    day_select_obj = Select(day_select_elem)
    time.sleep(3)
    day_select_obj.select_by_index(30)
    month_select_elem = driver.find_element(By.ID, 'month')
    month_select_obj = Select(month_select_elem)
    month_select_obj.select_by_visible_text('stu')
    time.sleep(3)
    year_select_elem = driver.find_element(By.ID, 'year')
    year_select_obj = Select(year_select_elem)
    year_select_obj.select_by_value('2022')
    time.sleep(3)
    assert 'No results found.' not in driver.page_source

