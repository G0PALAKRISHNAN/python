import os
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("file:///C:/Users/kk703.DESKTOP-J939SLP/Desktop/fileUpload.html")
driver.maximize_window()

upload = driver.find_element_by_xpath("//input[@name='resumeUpload']")
upload.click()

os.startfile("C:\\Users\\kk703.DESKTOP-J939SLP\\Desktop\\AutoIT\\SampleFileUpload.exe")
