from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.flipkart.com")
time.sleep(5)

driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
driver.find_element_by_xpath("//input[@name='q']").send_keys("iphone 6")
driver.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(5)

driver.find_element_by_xpath("//div[contains(text(),'Apple iPhone 6 (Space Grey, 32 GB)')]/../../..//input[@type='checkbox']").click()
#time.sleep(5)
#driver.close()