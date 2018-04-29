from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.implicitly_wait(30)
sleep(2)
driver.find_element_by_id("email").send_keys('kk7030@gmail.com')
driver.find_element_by_id("pass").send_keys('Kitty@2366')
driver.find_element_by_id("loginbutton").click()
sleep(5)

driver.close()