from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.gmail.com")
sleep(2)
driver.maximize_window()
sleep(1)
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("kk7030")
sleep(2)
driver.find_element_by_xpath("//div[@id='identifierNext']").click()
sleep(1)
driver.find_element_by_xpath("//input[@type='password']").send_keys("Kitty@2811")
sleep(2)
driver.find_element_by_xpath("//div[@id='passwordNext']").click()
sleep(10)
driver.find_element_by_xpath("((//table[@id=':3m'][@class='F cf zt']//tbody)/tr)[5]").click()

sleep(7)
driver.close()
