from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.bankbazaar.com/credit-score.html")
driver.maximize_window()
driver.implicitly_wait(30)

selectGender = driver.find_element_by_xpath("//span[@class='sprite-gender icon-gender-male']")
selectGender.click()
action = ActionChains(driver)
slider=driver.find_element_by_xpath("//div[@class='slider-handle round']")
age1=driver.find_element_by_xpath("//div[text()='18']")
action.click_and_hold(slider).pause(2)
action.drag_and_drop_by_offset(age1,70,150)   #drag_and_drop_by_offset(source, xoffset, yoffset)
#Holds down the left mouse button on the source element, then moves to the target offset and releases the mouse button.
action.perform()
sleep(1)
month = driver.find_element_by_xpath("//a[contains(text(),'Aug 1990')]")
month.click()
sleep(2)
date = driver.find_element_by_xpath("//a[contains(text(),'13')]")
date.click()
sleep(1)
dateCheck = driver.find_element_by_xpath("//input[@name='dob']")
print(dateCheck.get_attribute("value"))
if dateCheck.get_attribute("value") == '13 Aug 1990':
    print("Entered date is correct ")
else:
    print("Entered date is incorrect")
sleep(5)
driver.close()
