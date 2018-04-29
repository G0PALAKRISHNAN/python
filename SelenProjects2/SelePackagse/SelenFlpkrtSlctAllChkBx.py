from time import sleep

from pywinauto import mouse
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://www.flipkart.com")
driver.find_element_by_xpath("//input[@name='q']").send_keys("mobile")
driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
driver.find_element_by_xpath("//button[@class='vh79eN']").click()

checkBoxs = driver.find_elements_by_xpath("(//div[@class='_2SxMvQ']//input)")

for checkBox in checkBoxs:
    checkBox.click()
    sleep(1)

sleep(4)
driver.close()