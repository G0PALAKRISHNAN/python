from selenium import webdriver
from time import sleep
import autoit

driver = webdriver.Chrome()
driver.get("https://mail.google.com/")
driver.implicitly_wait(30)
driver.maximize_window()

driver.find_element_by_id("identifierId").send_keys("kk7030")
driver.find_element_by_id("identifierNext").click()
sleep(2)
driver.find_element_by_name("password").send_keys("Kitty@2811")
driver.find_element_by_id("passwordNext").click()
sleep(5)
driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
file_link = driver.find_element_by_xpath("//div[@id=':15h']") #Attachment link
file_link.click()
sleep(5)

autoit.win_activate("Open")
autoit.control_set_text("Open","Edit1","C:\\Users\\kk703.DESKTOP-J939SLP\\Desktop\\HTML Pages\\1. Topics.docx")
autoit.control_send("Open","Button1","{ENTER}")

file_name = driver.find_element_by_name("//a[@id=':17z']")
if file_name.text == "1. Topics.docx":
    print("Successfull")
else:
    print("failed")

driver.close()