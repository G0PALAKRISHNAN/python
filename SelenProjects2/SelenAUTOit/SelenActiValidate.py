import keyboard
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[@id='username']").send_keys("admin")
driver.find_element_by_xpath("//input[@name='pwd']").send_keys("manager")
driver.find_element_by_xpath("//a[@id='loginButton']").click()

driver.find_element_by_xpath("//div[contains(text(),'REPORTS')]/..").click()
driver.find_element_by_xpath("//div[contains(text(),'Monthly Team Performance')]").click()

driver.find_element_by_xpath("(//td[contains(text(),'Export to CSV')])[1]").click()
sleep(5)

keyboard.press_and_release('control+J')
sleep(5)
downloadedFile = driver.find_element_by_partial_link_text("actiTIME - Staff Performance (Feb 01, 2018 - Feb 28, 2018).csv")
print(downloadedFile.text)
# actiTIME - Staff Performance (Feb 01, 2018 - Feb 28, 2018).csv