from time import sleep

import keyboard
from selenium import webdriver

driver =webdriver.Chrome()
driver.get("http://docs.seleniumhq.com")
driver.maximize_window()
driver.implicitly_wait(30)
sleep(5)

keyboard.press_and_release('control+w')