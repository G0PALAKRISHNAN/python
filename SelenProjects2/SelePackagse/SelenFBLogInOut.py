from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
driver.maximize_window()
sleep(5)

driver.find_element_by_xpath("//input[@name='email']").send_keys("kk7030@gmail.com")
sleep(2)
driver.find_element_by_xpath("//input[@name='pass']").send_keys("Kitty@2811")
sleep(1)
driver.find_element_by_xpath("//label[@id='loginbutton']").click()
sleep(10)

'''alert = driver.switch_to.alert   #to handle the alert window
alert.accept()
sleep(4)
'''
driver.find_element_by_xpath("//div[@id='userNavigationLabel']").click()
sleep(3)
driver.find_element_by_xpath("(//ul[@class='_54nf'][@role='menu']//li)[12]").click()
sleep(10)
driver.close()