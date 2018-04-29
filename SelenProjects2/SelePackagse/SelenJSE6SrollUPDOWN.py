from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver =webdriver.Chrome()
driver.get("https://demo.vtiger.com")
'''driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  #WINDOW WILL SCROLL DOWN FROM TOP TO BOTTOM

sleep(5)

driver.execute_script("window.scrollTo(0,document.body.scrollTop)")  #WINDOW WILL SCROLL DOWN FROM BOTTOM TO TOP

sleep(5)'''

locator = driver.find_element_by_xpath("//h4[contains(text(),'new in Vtiger Cloud')]")
#driver.execute_script("arguments[0].scrollIntoView()",locator)
loc = locator.location
xCoordinates = loc.get('x')
yCoordinates = loc.get('y')
driver.execute_script("window.scrollBy(arguments[0],arguments[1])",xCoordinates,yCoordinates)
sleep(5)
driver.close()