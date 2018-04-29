from time import sleep
from PageClasses.LoginPage import Login_Page
from PageClasses.VerifyTasks import Verify_Tasks
from TestScripts.BaseTest import Base_Test
from PageClasses.HomePage import Home_Page
from PageClasses.TaskPage import Task_Page

base = Base_Test()
browser = base.launchBrowser('Chrome',"https://demo.actitime.com/",50)
loginPage = Login_Page(browser)
loginPage.login("admin","manager")
homePage = Home_Page(browser)
homePage.tasks()
taskPage = Task_Page(browser)
# taskPage.del_if_exists()
# browser.refresh()
taskPage.createNewTasks()
sleep(5)
browser.refresh()
verifytask = Verify_Tasks(browser)
verifytask.verifyTaskCreation()
base.closeBrowser()