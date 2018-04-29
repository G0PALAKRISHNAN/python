from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://airindia.com")
driver.maximize_window()
driver.implicitly_wait(50)

departing = driver.find_element_by_xpath("//input[@title='Departing']/..")
departing.click()

all_The_Dates = driver.find_elements_by_xpath("//span[text()='March']/../../..//tbody//tr//td//*")
#Printing all the dates of the selected month
for date in all_The_Dates:
    print(date.text)

sleep(5)
driver.close()