from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://demo.actitime.com")
driver.maximize_window()
driver.implicitly_wait(50)

driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
driver.find_element_by_xpath("//input[@name='pwd']").send_keys("manager")
driver.find_element_by_xpath("//a[@id='loginButton']").click()
firstName = "Kishan"
#//span[contains(text(),'Kashyap, Kishan')]
nameCheck = driver.find_element_by_xpath("//input[@placeholder='Start typing name']").send_keys(firstName)
listNames = driver.find_elements_by_xpath("//span[@class='userNameSpan']")
for listname in listNames:
    break
driver.find_element_by_xpath("//div[contains(text(),'USERS')]/..").click()
driver.find_element_by_xpath("//div[contains(text(),'Add User')]/..").click()
driver.find_element_by_xpath("//input[@name='firstName']").send_keys(firstName)
driver.find_element_by_xpath("//input[@name='lastName']").send_keys("Kashyap")
driver.find_element_by_xpath("//input[@name='email']").send_keys("kk7030@gmail.com")
driver.find_element_by_xpath("//input[@name='username']").send_keys("Kitty@")
driver.find_element_by_xpath("//input[@name='password']").send_keys("Kitty@1")
driver.find_element_by_xpath("//input[@name='passwordCopy']").send_keys("Kitty@1")
driver.find_element_by_xpath("//button[@id='ext-gen139']").click()
sleep(1)
driver.find_element_by_xpath("//li[@id='ext-gen180']").click()
driver.find_element_by_xpath("//input[@class='timeZonesSearchField']").send_keys("Bengaluru")
sleep(2)
driver.find_element_by_xpath("//div[@id='citiesSearchContainerElementId']//div").click()
sleep(1)
driver.find_element_by_xpath("//button[@id='ext-gen149']").click()
driver.find_element_by_xpath("(//table[@class='x-date-inner']//span[text()='1'])[1]").click()
driver.find_element_by_xpath("//span[contains(text(),'Create User')]/..").click()
