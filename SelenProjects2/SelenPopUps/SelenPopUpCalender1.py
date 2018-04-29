from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://airindia.com")
driver.maximize_window()
driver.implicitly_wait(50)

driver.find_element_by_xpath("//input[@title='Departing']").click()
all_the_Dates = driver.find_element_by_xpath("(//span[text()='April']/../../..//tbody//tr//td//*)[13]") #to select 13 of March
all_the_Dates.click()
sleep(5)
driver.close()