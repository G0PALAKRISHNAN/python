from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.bankbazaar.com/credit-score.html")
driver.maximize_window()
driver.implicitly_wait(30)

selectGender = driver.find_element_by_xpath("//span[@class='sprite-gender icon-gender-male']")
selectGender.click()

action = ActionChains(driver)
slider=driver.find_element_by_xpath("//div[@class='slider-handle round']")
age1 = driver.find_element_by_xpath("//div[text()='18']")
startOffset = age1.location
print(startOffset.get('x'),startOffset.get('y'))
sleep(10)
age2 = driver.find_element_by_xpath("//div[text()='27']")
#action.click_and_hold(age1).pause(1)
#startOffset = age1.location
endOffset = age2.location
print(endOffset)
print(endOffset.get('x'),endOffset.get('y'))
#startXCoord = startOffset.location.get('x')
#startYCoord = startOffset.location.get('y')
#action.drag_and_drop_by_offset(start)
#action.release().pause(2)
#action.perform()


driver.close()
#//div[@id='tooltip']