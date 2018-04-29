from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()
driver.get("http://docs.seleniumhq.com")
driver.maximize_window()
driver.implicitly_wait(30)

download =  driver.find_element_by_xpath("//a[@title='Get Selenium']")
download.send_keys(Keys.SHIFT + Keys.ENTER)
sleep(5)
handles = driver.window_handles

driver.switch_to.window(handles[1])
sleep(2)
driver.find_element_by_xpath("//a[text()='Maven users']").click()
sleep(5)
driver.quit()