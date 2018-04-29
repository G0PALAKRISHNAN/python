from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.orangecrm.com/")
driver.maximize_window()
sleep(5)

driver.find_element_by_xpath("//a[@class='dropdown-toggle']").click()
sleep(3)
driver.find_element_by_xpath("(//ul[@class='dropdown-menu']//li)[7]").click()
sleep(5)
driver.close()