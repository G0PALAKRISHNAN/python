import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(30)

links = driver.find_elements_by_tag_name('a')
print("Total number of Links in the Google Page :",len(links))
print("----------------------------------------------------------")
for link in links:
    print(link.get_attribute("href"))
print("----------------------------------------------------------")
driver.close()