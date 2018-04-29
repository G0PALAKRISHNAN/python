from time import sleep

from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get("https://mail.google.com/")
driver.implicitly_wait(30)
driver.maximize_window()

driver.find_element_by_id("identifierId").send_keys("kk7030")
driver.find_element_by_id("identifierNext").click()
sleep(2)
driver.find_element_by_name("password").send_keys("Kitty@2366")
driver.find_element_by_id("passwordNext").click()

driver.find_element_by_xpath("//div[contains(text(),'COMPOSE')]").click()
sleep(2)
file_link = driver.find_element_by_xpath("//div[@id=':15h']") #Attachment link
file_link.click()
sleep(2)
os.startfile("C:\\Users\\kk703.DESKTOP-J939SLP\\Desktop\\AutoIT\\FileUpload.exe")

filename = driver.find_element_by_xpath("//a[@id=':182']//div[1]")
if filename.text == "1. Topics.docx":
    print("File upload is successful")
else:
    print("File Upload is failed")

driver.close()