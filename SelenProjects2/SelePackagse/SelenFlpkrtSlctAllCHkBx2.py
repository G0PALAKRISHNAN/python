from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/search?q=phones&otracker=start&as-show=on&as=off")


#checkBoxes = driver.find_elements_by_xpath("//div[@class='GQtpzo']//div[@class='_1p7h2j']")
checkBoxes = driver.find_elements_by_xpath("//span[contains(text(),'Add to Compare')]/../..//input")

count = 0
num =0
for checkBox in checkBoxes:
    print(checkBoxes[count])
    driver.execute_script("arguments[0].click()",checkBoxes[count])
    count+=2
    num+=1
    sleep(2)
    if num == 4:
        sleep(10)
        driver.close()

sleep(10)
driver.close()