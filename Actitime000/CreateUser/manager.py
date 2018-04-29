from ActitimeUserScenario.ATUserS1 import driver
from time import sleep


def RegularUser(fName,lName,email,uName,pwd):
    driver.find_element_by_css_selector ("div.addUserButton.beigeButton.useNativeActive").click ()
    driver.find_element_by_css_selector ("input[name='firstName']").send_keys (fName)
    driver.find_element_by_css_selector ("input[name='lastName']").send_keys (lName)
    driver.find_element_by_css_selector ("input[name='email']").send_keys (email)
    driver.find_element_by_css_selector ("input[name='username']").send_keys (uName)
    driver.find_element_by_css_selector ("input[name='password']").send_keys (pwd)
    driver.find_element_by_css_selector ("input[name='passwordCopy']").send_keys (pwd)
    sleep (1)
    driver.find_element_by_xpath ("//div[@class=' at-dropdown-list-btn-ct ']//tbody").click ()
    sleep (1)
    driver.find_element_by_xpath ("//ul[@class='x-menu-list']//li[1]").click ()
    driver.find_element_by_xpath ("//div[@id='userDataLightBox_timeZonesSelectorPlaceholder']/input").send_keys (
        "Bengaluru")
    sleep (2)
    driver.find_element_by_xpath ("//span[contains(text(),'Bengaluru')]").click ()
    sleep (1)
    driver.find_element_by_xpath ("//div[@id='userDataLightBox_hireDate']/div[1]/..//button").click ()
    driver.find_element_by_xpath ("//button[contains(text(),'March 2018')]").click ()
    sleep (1)
    driver.find_element_by_xpath ("//a[contains(text(),'Jan')]").click ()
    driver.find_element_by_css_selector ("button.x-date-mp-ok").click ()
    sleep (1)
    driver.find_element_by_xpath ("//table[@class='x-date-inner']//tr[2]//td[2]").click ()
    driver.find_element_by_css_selector ("div.permissionsTemplatesMenuButton").click ()
    driver.find_element_by_xpath ("//div[contains(text(),'Manager')]").click ()
    driver.find_element_by_css_selector ("span.buttonTitle").click ()
