from time import sleep

from selenium.webdriver.support.select import Select

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.airindia.com")

dropDown = driver.find_element_by_id("ContentPlaceHolder1_UserLanguage1_drpCountry")
listBox = Select(dropDown)
listBox.select_by_visible_text('USA/Canada')
sleep(4)
dropDown1 = driver.find_element_by_id("ContentPlaceHolder1_UserLanguage1_ddlLanguage")
listBox1= Select(dropDown1)
listBox1.select_by_value('index-hnd.htm')
if listBox.is_multiple:
    print("Multi-Select drop down")
else:
    print("Single select Drop down")
sleep(5)

driver.quit()