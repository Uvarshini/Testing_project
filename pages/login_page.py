from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[@type='email']")
    continue_btn = (By.XPATH, "//button[contains(.,'Continue')]")
    password = (By.XPATH, "//input[@type='password']")
    login_btn = (By.XPATH, "//button[contains(.,'Login')]")

    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()