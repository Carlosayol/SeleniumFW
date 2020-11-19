from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    #Locators

    _signin_link = "//a[contains(text(),'Sign In')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def getSignInLink(self):
        return self.driver.find_element(By.XPATH,self._signin_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID,self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID,self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH,self._login_button)

    #Acciones

    def clickLoginLink(self):
        self.getSignInLink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, username="test@email.com", password="abcabc"):
        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()