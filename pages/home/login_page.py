from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username="test@email.com", password="abcabc"):
        loginLink = self.driver.find_element(By.XPATH,"//a[contains(text(),'Sign In')]")
        loginLink.click()

        emailForm = self.driver.find_element(By.ID,"email")
        emailForm.send_keys(username)

        passForm = self.driver.find_element(By.ID,"password")
        passForm.send_keys(password)

        loginButton = self.driver.find_element(By.XPATH,"//input[@value='Login']")
        loginButton.click()