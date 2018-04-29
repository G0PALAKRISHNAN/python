from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demo.vtiger.com")
time.sleep(5)
Content = driver.find_element_by_xpath("(//div[@class= 'marketingDiv widgetHeight']/div)[2]")
print(Content.text)

time.sleep(5)

driver.close()