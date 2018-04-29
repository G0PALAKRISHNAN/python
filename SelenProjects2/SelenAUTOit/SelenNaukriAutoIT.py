from selenium import webdriver
from time import sleep
import autoit

driver = webdriver.Firefox()
driver.get("https://www.naukri.com/")
driver.implicitly_wait(30)

driver.find_element_by_id("uploadBtnCont").click()

autoit.win_wait_active("File Upload",5)
autoit.control_set_text("File Upload","Edit1","C:\\Users\\kk703.DESKTOP-J939SLP\\Desktop\\Resume as on 06.3.18.docx")
sleep(3)
autoit.control_click("File Upload","Button1")
sleep(15)

result = driver.find_element_by_xpath("//span[contains(text(),' File uploaded successfully ')]")

if result.text == " File uploaded successfully ":
    print("Uploaded successfully")
else:
    print("Upload failed")
driver.quit()