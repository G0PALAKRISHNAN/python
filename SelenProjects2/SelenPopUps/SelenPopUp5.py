from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youvisit.com/tour/dartmouth/")
driver.implicitly_wait(50)

driver.find_element_by_xpath("(//div[@aria-label='Close registration'])[1]").click()
driver.find_element_by_xpath("(//div[@alt='Dartmouth Athletics'])[1]").click()
sleep(2)
driver.find_element_by_xpath("//div[@aria-label='Close registration']").click()
minimizedMap = driver.find_element_by_xpath("//div[@id='campusmap']")

action = ActionChains(driver)
action.move_to_element(minimizedMap).perform()

mapPlusButton = driver.find_element_by_xpath("//div[@id='map_plus_button']")

if mapPlusButton.is_displayed():
    print("PASS : Map is maximized")
else:
    print("FAIL : MAp is not maximized")
sleep(5)
driver.close()