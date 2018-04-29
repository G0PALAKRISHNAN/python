from time import sleep

from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://docs.seleniumhq.org")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@title='Get Selenium']").click()
driver.find_element_by_link_text("Javadoc").click()
frameEle = driver.find_element_by_xpath("//frame[@src='overview-summary.html']")
sleep(3)
#frameEle = driver.find_element_by_xpath("//frame[@src='packageListFrame']")  #web element as a inpt to frame identiication
driver.switch_to.frame("packageListFrame")
driver.find_element_by_xpath("(//ul[@title='Packages']//li)[1]")

sleep(3)
driver.close()