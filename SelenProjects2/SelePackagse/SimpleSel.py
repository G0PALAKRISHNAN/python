from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()

driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME, "pwd").send_keys("manager")
driver.find_element_by_id("loginButton").click()

sleep(5)
driver.close()