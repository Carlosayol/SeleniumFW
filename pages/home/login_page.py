from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _signin_link = "//a[contains(text(),'Sign In')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    # def getSignInLink(self):
    #     return self.driver.find_element(By.XPATH, self._signin_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.XPATH, self._login_button)

    # Acciones

    def clickLoginLink(self):
        self.elementClick(self._signin_link, locatorType="XPATH")

    def enterEmail(self, email):
        self.sendElementKeys(self._email_field, email)

    def enterPassword(self, password):
        self.sendElementKeys(self._password_field, password)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    # Funcionalidad

    def login(self, username="test@email.com", password="abcabc"):
        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()


    def verifyCorrectLogin(self):
        result = self.isElementPresent("//input[@id='search']",locatorType="XPATH")
        return result

    def verifyFailedLogin(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try again')]",
                                       locatorType="xpath")
        return result

    def verifyTitle(self):
        print("Pruebass: ",self.getTitle())
        if "All Courses" in self.getTitle():
            return True
        else:
            return False