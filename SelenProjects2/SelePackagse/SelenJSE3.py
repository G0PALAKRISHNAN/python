from selenium import  webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.actitime.com")
response = driver.execute_script("return document.getElementById('demoCredentials').textContent")
print("text of an element :", response)
driver.close()