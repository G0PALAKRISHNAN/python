from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
time.sleep(5)

#driver.find_element_by_xpath("//input[@id='username']").send_keys("admin")
driver.find