from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.actimind.com")
driver.implicitly_wait(30)

areaOf = driver.find_element_by_xpath("//a[@href='areas-expertise.html ']")

action = ActionChains(driver)
action.move_to_element(areaOf)
action.perform()

driver.close()