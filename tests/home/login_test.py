import pytest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest


@pytest.mark.usefixtures("ModulesetUp", "setUp")
class LoginTest(unittest.TestCase):

    # Class setup
    @pytest.fixture(autouse=True)
    def classSetup(self, ModulesetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # 2 test cases
    # result2 verify the title
    # result1 verify the login
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login()
        result2 = self.lp.verifyLoginTitle()
        self.ts.mark(result2, "Title verification")
        result1 = self.lp.verifyCorrectLogin()
        self.ts.markFinal("test_validLogin",result1,"Login verification")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login(username="test@hotmail.com", password="aassss")
        result = self.lp.verifyFailedLogin()
        self.ts.markFinal("test_invalidLogin",result,"Login verification")
