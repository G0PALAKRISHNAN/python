#Using
'''
CSS selector
by attributes
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()

driver.find_element_by_css_selector("input[name='username']").send_keys("admin")
driver.find_element_by_css_selector("input[name='pwd']").send_keys('manager')
driver.find_element_by_css_selector("a[id='loginButton']").click()

sleep(5)
driver.close()