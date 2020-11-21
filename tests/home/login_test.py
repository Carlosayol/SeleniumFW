from selenium import webdriver
import pytest
from pages.home.login_page import LoginPage
import unittest
import time

class LoginTest(unittest.TestCase):
    baseUrl = "https://courses.letskodeit.com"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(3)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login()
        result = self.lp.verifyCorrectLogin()

        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseUrl)
        self.lp.login(username="test@hotmail.com",password="aassss")

        result = self.lp.verifyFailedLogin()

        assert result == True



