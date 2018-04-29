from selenium import webdriver
from CreateUser.regularUser import createRegularUser


driver = webdriver.Chrome() #Browser driver initiation
driver.get("https://demo.actitime.com")  #Entering URl
driver.maximize_window()  #Browser Maximized
driver.implicitly_wait(30)  #Conditional Wait

#Logging into the Actitime application using Admin credentials
driver.find_element_by_css_selector("input#username").send_keys("admin")
driver.find_element_by_css_selector("input.textField.pwdfield").send_keys("manager")
driver.find_element_by_css_selector("a#loginButton").click()

driver.find_element_by_css_selector("a.content.users").click()

#Calling pre-definded function for creating Normal user
createRegularUser("Kishan","Kashyap","kk7030@gmail.com","Kitty@","Kitty@2366")

userNames = driver.find_elements_by_xpath("(//span[@class='userNameSpan'])")
uName = "Kashyap, Kishan"
for userName in userNames:
    if userName.text == uName:
        print("User created")
        break

# driver.find_element_by_xpath("//input[@class='filterFieldInput inputFieldWithPlaceholder']").send_keys(uName)
