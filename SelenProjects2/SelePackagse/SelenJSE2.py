from selenium import  webdriver

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")

A=5
response = driver.execute_script("return console.log('Value of A is : arguments[0]')",A)
print("Response from the browser console window after printing the value :", response)

driver.close()