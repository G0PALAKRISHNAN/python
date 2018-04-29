from selenium.webdriver.common.by import By
from PageClasses.BasePage import Base_Page


class Login_Page(Base_Page):

    def __init__(self,driver):
        Base_Page.__init__(self,driver)

    Object_Repository = {
        "userName":(By.ID, "username"),
        "password" : (By.NAME, "pwd"),
        "login" : (By.ID, "loginButton")
        }

    def login(self, user_name, pass_word):
        self.find_element(*self.Object_Repository['userName']).send_keys(user_name)
        self.find_element(*self.Object_Repository['password']).send_keys(pass_word)
        self.find_element(*self.Object_Repository['login']).click()