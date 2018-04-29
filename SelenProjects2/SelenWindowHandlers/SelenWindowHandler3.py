from time import sleep

import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()
driver.get("http://docs.seleniumhq.com")
driver.maximize_window()
driver.implicitly_wait(30)

download =  driver.find_element_by_xpath("//a[@title='Get Selenium']")
download.send_keys(Keys.CONTROL + Keys.ENTER)
parent_Window_Handle = driver.current_window_handle
new_Window_Handle = None

handles = driver.window_handles

for handle in handles:
    if handle != parent_Window_Handle:
        new_Window_Handle = handle
        break

driver.switch_to.window(new_Window_Handle)
sleep(5)
driver.find_element_by_xpath("//a[text()='Maven users']").click()
sleep(5)

driver.quit()