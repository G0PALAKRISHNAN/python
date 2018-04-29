from time import sleep
from selenium import webdriver

class Base_Test (object):

    def __init__(self):
        self.driver = None

    def launchBrowser(self, Browser_Name, Url, time):
        if Browser_Name == 'Chrome':
            self.driver = webdriver.Chrome ()
        else:
            self.driver = webdriver.Firefox ()
        self.driver.maximize_window ()
        self.driver.get (Url)
        self.driver.implicitly_wait (time)
        return self.driver

    def closeBrowser(self):
        sleep (5)
        self.driver.quit ()
