from selenium import webdriver
import time

import  key
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
time.sleep(2)

pointer = driver.find_element_by_tag_name('body')
pointer.send_keys(Keys.CONTROL + 'T')
time.sleep(5)

driver.close()
