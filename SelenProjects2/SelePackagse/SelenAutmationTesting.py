from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/")
driver.maximize_window()
sleep(5)

driver.find_element_by_xpath("//img[@id='enterimg']").click()
Text = driver.find_element_by_xpath("//div[@class='col-sm-8 col-xs-8 col-md-8']//h1").text

print(Text)
sleep(5)

driver.close()
