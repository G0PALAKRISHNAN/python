from selenium import webdriver
from time import sleep
import autoit

driver =webdriver.Firefox()
driver.get("https://www.seleniumhq.org/download/")
driver.implicitly_wait(30)

link = driver.find_element_by_xpath("//a[contains(text(),'3.10.0')]")
link.click()

autoit.win_activate("Opening selenium-server-standalone-3.10.0.jar")
autoit.send("{ENTER}")

sleep(5)
driver.close()