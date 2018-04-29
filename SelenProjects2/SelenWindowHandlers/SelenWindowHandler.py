from selenium import webdriver


driver =webdriver.Chrome()
driver.get("http://docs.seleniumhq.com")
driver.maximize_window()
driver.implicitly_wait(30)

download =  driver.find_element_by_xpath("//a[@title='Get Selenium']")

print(driver.current_window_handle)

driver.close()