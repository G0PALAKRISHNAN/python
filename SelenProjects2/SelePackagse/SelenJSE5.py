from time import sleep

from selenium import  webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.actitime.com")

response = driver.execute_script("return document.getElementById('loginButton').click()")
print(response)

sleep(5)
driver.close()