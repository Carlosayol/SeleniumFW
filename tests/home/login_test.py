import pytest
from pages.home.login_page import LoginPage
import unittest


@pytest.mark.usefixtures("ModulesetUp", "setUp")
class LoginTest(unittest.TestCase):

    # Class setup
    @pytest.fixture(autouse=True)
    def classSetup(self, ModulesetUp):
        self.lp = LoginPage(self.driver)

    # 2 test cases
    # result2 verify the title
    # result1 verify the login
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login()
        result2 = self.lp.verifyTitle()
        assert result2 == True

        result1 = self.lp.verifyCorrectLogin()
        assert result1 == True


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login(username="test@hotmail.com", password="aassss")
        result = self.lp.verifyFailedLogin()
        assert result == True

    # New test class