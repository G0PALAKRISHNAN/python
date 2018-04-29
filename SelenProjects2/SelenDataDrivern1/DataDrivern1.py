from time import sleep

from selenium import webdriver
import pandas as PD

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()
driver.implicitly_wait(30)

file_path = "C:\\Users\\kk703.DESKTOP-J939SLP\\Desktop\\Data\\TestData.xlsx"
excel = PD.read_excel(file_path, sheet_name="Sheet1")
Username = excel['UserName'][0]
Password = excel['Password'][1]
ExpectedResults = excel['Expected_result'][0]

driver.find_elements("username").send_keys(Username)
driver.find_element_by_name("pwd").send_keys(Password)
driver.find_element_by_id("loginButton").click()

sleep(9)
titleOfHomepage = driver.title

if titleOfHomepage == ExpectedResults:
    print("PASS: Login to the Application")
else:
    print("FAIL: Login Failed")

driver.close()