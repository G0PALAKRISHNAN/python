#css selector by ID

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()

driver.find_element_by_css_selector("input#username").send_keys("admin") #CSS ID
driver.find_element_by_css_selector("input.textField.pwdfield").send_keys("manager")  #CSS CLASS
driver.find_element_by_css_selector("a[id='loginButton']>div").click()  #CSS CHILD

sleep(5)
driver.close()