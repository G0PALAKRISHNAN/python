from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://airindia.com")
driver.maximize_window()
driver.implicitly_wait(50)

departing = driver.find_element_by_xpath("//input[@title='Departing']/..")
departing.click()

firstMonth = driver.find_element_by_xpath("(//div[@id='ui-datepicker-div']//div//div//div//span)[1]")
secMonth = driver.find_element_by_xpath("(((//div[@class='ui-datepicker-group ui-datepicker-group-last'])//div)//div//span)[1]")
sleep(2)

if firstMonth.text == "May" or secMonth.text == "May":
    month_date = driver.find_element_by_xpath("(//span[text()='May']/../../..//tbody//tr//td//*)[22]")
    month_date.click()
else:
    nextButton = driver.find_element_by_xpath("//span[text()='Next']")
    nextButton.click()
    sleep(2)
    month_date = driver.find_element_by_xpath("(//span[text()='May']/../../..//tbody//tr//td//*)[22]")
    month_date.click()

sleep(5)
driver.close()