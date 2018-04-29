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
all_Window_Handles = driver.window_handles

for handles in all_Window_Handles:
    print(handles)

driver.quit()