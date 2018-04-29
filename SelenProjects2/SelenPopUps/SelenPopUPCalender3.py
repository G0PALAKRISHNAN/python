from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://airindia.com")
driver.maximize_window()
driver.implicitly_wait(50)

departing = driver.find_element_by_xpath("//input[@title='Departing']/..")
departing.click()

# * will select any tags after the previous tag, irrespective of child tags
all_The_Dates = driver.find_elements_by_xpath("//span[text()='March']/../../..//tbody//tr//td//*")
#Checking whether the dates are Enabled or Disabled & Printing them.
for date in all_The_Dates:
    if date.is_enabled():
        print(date.text,': Enabled')
    else:
        print(date.text,': Disabled')
sleep(5)
driver.close()