from selenium.webdriver.support.select import Select

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///")

multiDropDown = driver.find_element_by_name("mobDevices")
select = Select(multiDropDown)

allOptions = Select.options

for allOption in allOptions:
    print(allOption.text)

driver.close()