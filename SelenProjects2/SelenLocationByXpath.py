from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
time.sleep(5)

Login = driver.find_element_by_xpath("//a[@class='initial']")


print("Co ordinates of login : " , Login.location)
print("X co ordinate of Login Button is : ", Login.location.get('x'))
print("Y co ordinate of Login Button is : ", Login.location.get('y'))

time.sleep(3)
driver.close()