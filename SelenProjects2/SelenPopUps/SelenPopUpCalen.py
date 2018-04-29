from selenium import webdriver
from time import sleep

month = input("Enter the month ")
date = input("Enter the Date")

driver = webdriver.Chrome()
driver.get("http://airindia.com")
driver.maximize_window()
driver.implicitly_wait(50)

departing = driver.find_element_by_xpath("//input[@title='Departing']/..")
departing.click()
#For visual Purpose I've used Sleeps
firstMonth = driver.find_element_by_xpath("(//div[@id='ui-datepicker-div']//div//div//div//span)[1]")
secMonth = driver.find_element_by_xpath("(((//div[@class='ui-datepicker-group ui-datepicker-group-last'])//div)//div//span)[1]")
sleep(2)
if firstMonth.text == month or secMonth.text == month:
    month_date = driver.find_element_by_xpath("(//span[text()='"+month+"']/../../..//tbody//tr//td//*)["+date+"]")
    month_date.click()
else:
    for m in range(0,12):
        nextButton = driver.find_element_by_xpath("//span[text()='Next']")
        nextButton.click()
        sleep(0.5)
        nextButton = driver.find_element_by_xpath("//span[text()='Next']")
        nextButton.click()
        sleep(1)
        m+=1
        firstMonth = driver.find_element_by_xpath("(//div[@id='ui-datepicker-div']//div//div//div//span)[1]")
        secMonth = driver.find_element_by_xpath("(((//div[@class='ui-datepicker-group ui-datepicker-group-last'])//div)//div//span)[1]")
        if firstMonth.text == month or secMonth.text == month:
            sleep(1)
            month_date = driver.find_element_by_xpath("(//span[text()='"+month+"']/../../..//tbody//tr//td//*)["+date+"]")
            month_date.click()
            break

'''bookingDate = driver.find_element_by_xpath("//input[@title='Departing']/..")
print("The booking Date is : ",bookingDate.text)'''

sleep(5)
driver.close()