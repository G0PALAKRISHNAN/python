from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
login=driver.find_element_by_id("loginButton")
login.send_keys(Keys.ENTER)
sleep(10)

driver.close()