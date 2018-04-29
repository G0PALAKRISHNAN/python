from time import sleep

from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://docs.seleniumhq.org")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@title='Get Selenium']").click()
driver.find_element_by_link_text("Javadoc").click()
frameEle = driver.find_element_by_xpath("//frame[@src='overview-summary.html']")  #web element as a inpt to frame identiication
#priority is given in order. 1. ID/NAME   2. XPATH   3.INDEX
#driver.switch_to.frame("classFrame")    #ID/NAME is given as input to the frame switching
#driver.switch_to.frame(2)  #indexing stats from 0,1,2. as the this frame is 3rd one so we give 2 as input
driver.switch_to.frame(frameEle)
driver.find_element_by_xpath("(//a[text()='Frames'])[1]").click()
sleep(3)
driver.close()