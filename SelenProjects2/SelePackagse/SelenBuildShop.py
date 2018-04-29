from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://buildshop.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_css_selector("a.NsigninButton").click()
driver.find_element_by_css_selector("input#ctl00_ContentPlaceHolder1_Login101_UserName").send_keys("sushma.jb82@gmail.com")
driver.find_element_by_css_selector("input#ctl00_ContentPlaceHolder1_Login101_Password").send_keys("Qspiders$1")
driver.find_element_by_css_selector("a.signinP").click()

driver.find_element_by_css_selector("div#ctl00_ServiceModule1_pnlCustomers").click()
driver.find_element_by_css_selector("input#ctl00_MainContent_btnNew").click()
driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_txtContactName").send_keys("Kitty")
firstName = "Kishan"
driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_txtFirstName").send_keys(firstName)
driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_PhoneTextBox").send_keys("9591713241")
driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_EmailTextBox").send_keys("kk7030@gmail.com")
driver.find_element_by_css_selector("input#ctl00_MainContent_FormViewContactInsert_InsertButton").click()
driver.execute_script("window.scrollTo(0,top)")
driver.find_element_by_css_selector("input#ctl00_MainContent_btnBack").click()

sleep(5)
names = driver.find_elements_by_css_selector("span[id*='FirstName']")
for name in names:
    if name.text == firstName:
        print("Username "+firstName+" created Succesfully and found in the Contacts")
        break
driver.close()