from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()
driver.implicitly_wait(30)

userName = driver.find_element_by_id('username')
userName.send_keys('admin')
print("Username address is ",userName)

driver.refresh()

userName1 = driver.find_element_by_id('username')

print("Username address is ",userName1)
userName1.clear()
userName1.send_keys('uhuhuhu')