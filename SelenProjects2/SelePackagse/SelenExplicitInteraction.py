from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://docs.seleniumhq.org")
driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@title='Get Selenium']").click()
driver.find_element_by_link_text("Javadoc").click()
frameEle = driver.find_element_by_xpath("//frame[@src='overview-summary.html']")
waitFor = WebDriverWait(driver,30)
response = waitFor.until(EC.frame_to_be_available_and_switch_to_it(frameEle))
print(response)
texts = driver.find_element_by_xpath("//div[@class='contentContainer']").text
print(texts)
driver.switch_to.default_content()
driver.switch_to.frame("packageListFrame")
driver.find_element_by_xpath("//a[@href='com/thoughtworks/selenium/package-frame.html']").click()
sleep(4)
driver.close()