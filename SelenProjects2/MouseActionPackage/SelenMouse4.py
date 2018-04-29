from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://istqb.in")
driver.implicitly_wait(30)

foundation = driver.find_element_by_xpath("//span[text()='FOUNDATION']")
enrollment = driver.find_element_by_xpath("//a[@id='menu775']")
corporateEnrollent = driver.find_element_by_xpath("//a[@id='menu777']")
onlineEnrollent = driver.find_element_by_xpath("//a[@id='menu779']")

action = ActionChains(driver)
action.move_to_element(foundation).pause(1).move_to_element(enrollment).pause(1)
action.move_to_element(corporateEnrollent).pause(1).click(onlineEnrollent).perform()

sleep(5)
driver.close()