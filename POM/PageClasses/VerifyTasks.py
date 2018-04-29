from time import sleep

from selenium.webdriver.common.by import By

from PageClasses.BasePage import Base_Page


class Verify_Tasks(Base_Page):

    def __init__(self, driver):
        Base_Page.__init__(self, driver)

    Object_Repository = {
        "verifytask": (By.XPATH,"//table[@class='taskRowsTable']//div[@class='title ellipsis']")
    }

    def verifyTaskCreation(self):
        # taskLists = self.driver.find_elements_by_xpath("//table[@class='taskRowsTable']//div[@class='title ellipsis']")
        taskLists = self.find_elements(*self.Object_Repository['verifytask'])
        for taskList in taskLists:
            if taskList.text == 'Amplifier':
                print("Task Amplifier is Created Successfully")
                break