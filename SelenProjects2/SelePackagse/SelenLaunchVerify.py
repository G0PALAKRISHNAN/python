from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.orangecrm.com/")
driver.maximize_window()
sleep(10)

if driver.title == "CRM Web Based Enterprise Solution | OrangeCRM":
    print("Orange main page is displayed")
    sleep(5)
    driver.get_screenshot_as_file("..//screenshot1.png")
    driver.find_element_by_xpath("//a[contains(text(),'FEATURES')]").click()
else:
    print("The Required page is not displayed")

sleep(1)
content = driver.find_element_by_xpath("(//div[@class='col-md-6']/../div)[2]").text
print(content)

driver.close()