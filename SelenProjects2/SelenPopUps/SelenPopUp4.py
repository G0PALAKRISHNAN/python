from time import sleep
from selenium import webdriver
import random
import string

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youvisit.com/tour/dartmouth")
driver.implicitly_wait(50)

driver.find_element_by_xpath("//div[@id='registration-visitortype']").click()
sleep(1)
driver.find_element_by_xpath("//td[@item-value='prospective_student']").click()
sleep(1)
driver.find_element_by_xpath("(//div[@class='grid child-grid show']//td)[1]").click()
#RandomName =  ''.join(random.choice(string.ascii_uppercase) for x in range(10))
driver.find_element_by_xpath("//input[@id='firstname']").send_keys("Kishan")  #First name
driver.find_element_by_xpath("//input[@id='lastname']").send_keys("Kashyap")  #Last name
driver.find_element_by_xpath("//input[@id='email']").send_keys("kk7030@gmail.com")  #Email ID

#Selecting the Enrollment Year by using Select method
enrollYear = driver.find_element_by_id("enrollyear")
select = Select(enrollYear)
select.select_by_value('2018')
#Selecting Current school by Select method
driver.find_element_by_xpath("//input[@id='school']").send_keys("Romero")
sleep(2)
driver.find_element_by_xpath("(//ul[@id='ui-id-1']//li)[1]").click()
#Selecting Major Subject by using Select Method
major = driver.find_element_by_id("major")
select1 = Select(major)
select1.select_by_value('Computer Science')
#Selecting the Gender by using Select method
gender = driver.find_element_by_id("gender")
select2 = Select(gender)
select2.select_by_value('Male')
#Selecting DOB by select method for month and year
driver.find_element_by_xpath("//div[@id='registration-birthdate']").click()
selectMonth = driver.find_element_by_class_name("ui-datepicker-month")
selectM = Select(selectMonth)
selectM.select_by_value('7')
selectYear = driver.find_element_by_class_name("ui-datepicker-year")
selectY = Select(selectYear)
selectY.select_by_value('1990')
#selecting the Date by inspecting normal XPath web element
driver.find_element_by_xpath("((//table[@class='ui-datepicker-calendar']//tbody//tr)[3]//td)[2]").click()
#Inputting mobile number
driver.find_element_by_xpath("//input[@id='phone']").send_keys("9972524240")
#Selecting Country by using Select method
country = driver.find_element_by_id('country')
selectCountry = Select(country)
selectCountry.select_by_value("IND")
#Giving address
driver.find_element_by_xpath("//input[@id='intl_street']").send_keys("Near Shopper Stop, Bannerghatta Road")
driver.find_element_by_xpath("//input[@id='intl_city']").send_keys("Bangalore")
driver.find_element_by_xpath("//input[@id='intl_state']").send_keys("Karnataka")
driver.find_element_by_xpath("//input[@id='intl_postal']").send_keys("560076")


print("Data Successfully Inserted")
sleep(2)
driver.close()