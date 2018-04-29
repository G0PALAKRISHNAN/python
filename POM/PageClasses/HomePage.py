from selenium.webdriver.common.by import By

from PageClasses.BasePage import Base_Page


class Home_Page(Base_Page):

    def __init__(self, driver):
        Base_Page.__init__(self, driver)

    Object_Repository = {
        "Task": (By.XPATH, "//div[text()='TASKS']/.."),
    }

    def tasks(self):
        self.find_element(*self.Object_Repository["Task"]).click()
