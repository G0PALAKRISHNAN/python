from selenium import  webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.actitime.com")


response = driver.execute_script(" return document.getElementById('username').value='admin'")
print(response)
driver.execute_script(" return document.getElementsByName('pwd').value='manager'")


driver.close()