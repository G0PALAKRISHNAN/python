from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
time.sleep(5)

Username = driver.find_element_by_xpath("//input[contains(@id,'username')]")
Password = driver.find_element_by_xpath("//input[contains(@name,'pwd')]")

Login = driver.find_element_by_xpath("//a[@class='initial']")


Username.send_keys("admin")
Password.send_keys("manager")

print("Username is ",Username.get_attribute('value'))
print("Password is ",Password.get_attribute('value'))
print("Value of login : " , Login.get_attribute('id'))

time.sleep(5)
driver.close()