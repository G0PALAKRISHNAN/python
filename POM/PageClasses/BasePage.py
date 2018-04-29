class Base_Page(object):

    def __init__(self, driver):
        self.driver= driver
        self.driver.set_page_load_timeout(40)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)