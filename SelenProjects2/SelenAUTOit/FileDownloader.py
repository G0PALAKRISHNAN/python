from selenium import webdriver
from time import sleep

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip") #Avoids displaying the alerts
profile.set_preference("browser.download.folderList",0) # saves the file to desktop instead of Default folder(Download)

driver = webdriver.Firefox(profile)
driver.get("https://www.seleniumhq.org/download/")
driver.implicitly_wait(30)

downloadLink = driver.find_element_by_xpath("//td[text()='Java']/..//a[text()='Download']")
downloadLink.click()