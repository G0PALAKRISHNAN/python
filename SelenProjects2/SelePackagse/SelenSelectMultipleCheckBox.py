from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///C:/Users/kk703.DESKTOP-J939SLP/Desktop/HTML%20Pages/Checkbox.html")
driver.implicitly_wait(30)

checkBoxs = driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkBox in checkBoxs:
    checkBox.click()
    sleep(1)

driver.close()