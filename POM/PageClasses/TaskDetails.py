from time import sleep
class Task_Details_Page():

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(30)

    def createTask(self):
        self.driver.find_element_by_xpath("//div[@id='createTasksPopup_customerSelector']//tr//button").click()
        # self.__CustOpt.click()
        self.driver.find_element_by_xpath("//ul[@class='x-menu-list']//li[5]").click()
        # self.__CustSel.click()
        self.driver.find_element_by_xpath("//div[@id='createTasksPopup_projectSelector']//tr//button").click()
        # self.__ProjOpt.click()
        self.driver.find_element_by_xpath("//ul[@class='x-menu-list']//li[11]").click()
        # self.__ProjSel.click()
        self.driver.find_element_by_xpath("(//*[@id='createTasksPopup_createTasksTableContainer']/table/tbody//input)[1]").send_keys('Task!')
        # self.__TaskName.send_keys('Task!')
        self.driver.find_element_by_xpath("(//div[@id='createTasksPopup_createTasksTableContainer']/table//tbody//a)[1]").click()
        # self.__TaskDesc.click()
        self.driver.find_element_by_xpath("//div[@id='editDescriptionPopupEditingState']").send_keys('abcdwxyz')
        # self.__TaskDescDet.send_keys('abcdwxyz')
        self.driver.find_element_by_xpath("//*[@id='scbutton']").click()
        # self.__TaskDescSave.click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='createTasksPopup_commitBtn']/div/span").click()
        # self.__TaskSave.click()

