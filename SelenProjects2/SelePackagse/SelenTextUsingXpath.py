from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
time.sleep(5)

Credentials = driver.find_element_by_id("demoTooltipContainer")

print(Credentials.text)

time.sleep(5)
driver.close()