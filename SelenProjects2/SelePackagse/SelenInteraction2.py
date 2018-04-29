from selenium.webdriver.support.select import Select

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///")

multiDropDown = driver.find_element_by_name("mobDevices")
select = Select(multiDropDown)

select.select_by_index(3)
select.select_by_visible_text('iPhone')
select.select_by_value('5')

selectedOptions = Select.all_selected_options

for selectedOption in selectedOptions:
    print(selectedOption.text)

driver.close()