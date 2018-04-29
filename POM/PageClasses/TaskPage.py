from time import sleep
from selenium.webdriver.common.by import By
from PageClasses.BasePage import Base_Page

class Task_Page(Base_Page):

    def __init__(self, driver):
        Base_Page.__init__(self, driver)

    delTask=None
    Object_Repository = {
        "addNewTask": (By.XPATH, "//div[contains(text(),'Add New Task')]"),
        "createTask": (By.XPATH, "//div[contains(text(),'Create new tasks')]"),
        # "custOpt": (By.XPATH, "//div[@id='createTasksPopup_customerSelector']//button"),
        # "custSel": (By.XPATH, "(//a[contains(text(),'Boston Chocolate')]/..)[2]"),
        # "projOpt": (By.XPATH, "//div[@id='createTasksPopup_projectSelector']//td"),
        # "projSel": (By.XPATH, "//a[contains(text(),'Web site creation')]/.."),
        "taskName": (By.XPATH, "(//input[@class='inputFieldWithPlaceholder'])[1]"),
        "taskDesc": (By.XPATH, "(//input[@class='inputFieldWithPlaceholder']/../..//table)[1]"),
        "taskDescDet": (By.XPATH, "//textarea[@id='editDescriptionPopupText']"),
        "taskDescSave": (By.XPATH, "//input[@id='scbutton']"),
        "taskSave": (By.XPATH, "//span[contains(text(),'Create Tasks')]/.."),
        # "taskToBeDel" : (By.XPATH, "//table[@class='taskRowsTable']//div[@class='title ellipsis'][contains(text(),'Amplifier')]"),
        # "delIfExists": (By.XPATH, "//table[@class='taskRowsTable']//div[@class='title ellipsis'][contains(text(),'Amplifier')]/../../..//div/div"),
        # "delItem" : (By.XPATH, "//div[@class='deleteButton']"),
        # "confirmDelItem" : (By.XPATH, "//*[@id='deleteTaskPopup_deleteConfirm_submitBtn']")
        # "tasks": (By.XPATH, "//table[@class='taskRowsTable']//div[@class='title ellipsis']"),
    }

    # def del_if_exists(self):
    #     sleep(2)
    #     self.delTask = self.find_element(*self.Object_Repository['taskToBeDel'])
    #     if self.delTask.
    #     self.find_element(*self.Object_Repository['delIfExists']).click()
    #     sleep(2)
    #     self.find_element(*self.Object_Repository['delItem']).click()
    #     sleep(2)
    #     self.find_element(*self.Object_Repository['confirmDelItem']).click()

    def createNewTasks(self):
        sleep(2)
        self.find_element(*self.Object_Repository['addNewTask']).click()
        self.find_element(*self.Object_Repository['createTask']).click()
        # self.find_element(*self.Object_Repository['custOpt']).click()
        # self.find_element(*self.Object_Repository['custSel']).click()
        # self.find_element(*self.Object_Repository['projOpt']).click()
        # self.find_element(*self.Object_Repository['projSel']).click()
        self.find_element(*self.Object_Repository['taskName']).send_keys('Amplifier')
        self.find_element(*self.Object_Repository['taskDesc']).click()
        sleep(1)
        self.find_element(*self.Object_Repository['taskDescDet']).send_keys('Details of the project')
        sleep(1)
        self.find_element(*self.Object_Repository['taskDescSave']).click()
        self.find_element(*self.Object_Repository['taskSave']).click()