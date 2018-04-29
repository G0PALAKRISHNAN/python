from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
time.sleep(5)

Username = driver.find_element_by_xpath("//input[contains(@id,'username')]")
Password = driver.find_element_by_xpath("//input[contains(@name,'pwd')]")

print("Enterting the credentials")
Username.send_keys("admin")
Password.send_keys("manager")
time.sleep(5)

print("Clearing the text")
Username.clear()
Password.clear()
time.sleep(3)

print("Entering the Credentials again")
Username.send_keys("Kishan")
Password.send_keys("Manager")

time.sleep(5)
driver.close()