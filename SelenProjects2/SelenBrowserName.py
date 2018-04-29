from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
sleep(5)
name = driver.name
print(name)
sleep(4)
driver.close()