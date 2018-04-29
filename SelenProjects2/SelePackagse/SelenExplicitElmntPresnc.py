from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://demo.actitime.com")

wait = WebDriverWait(driver,30)
element = wait.until(EC.presence_of_element_located((By.ID, 'loginButton')))
element.click()
print(element)

driver.close()