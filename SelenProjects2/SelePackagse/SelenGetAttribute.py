from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demo.vtiger.com")
time.sleep(5)

Username = driver.find_element_by_xpath("//input[contains(@id,'username')]")
Password = driver.find_element_by_xpath("//input[contains(@id,'password')]")

print("Username is :",Username.get_attribute('value'))
print("Password is :",Password.get_attribute('value'))

time.sleep(5)
driver.close()