import keyboard
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.seleniumhq.org/download/")
driver.maximize_window()
driver.implicitly_wait(30)

link = driver.find_element_by_xpath("//a[contains(text(),'3.10.0')]")
link.click()
sleep(5)

keyboard.press("left")
keyboard.press("enter")

sleep(20)
driver.close()