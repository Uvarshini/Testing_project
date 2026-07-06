from selenium.webdriver.common.by import By

class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")

    def enter_first_name(self, name):
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_last_name(self, name):
        self.driver.find_element(*self.last_name).send_keys(name)