from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
time.sleep(5)

driver.find_element_by_xpath("//input[contains(@id,'username')]").send_keys("admin")
driver.find_element_by_xpath("//input[contains(@name,'pwd')]").send_keys("manager")
checkBox = driver.find_element_by_id("keepLoggedInCheckBox")
loginButton = driver.find_element_by_xpath("(//div[contains(text(),'Login')])[1]")

if loginButton.is_displayed():
    print("Login button is displayed")
    checkBox.click()
    loginButton.click()
else:
    print("Error : Login button is not displayed")

time.sleep(5)
driver.close()