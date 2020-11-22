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
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login()
        result = self.lp.verifyCorrectLogin()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login(username="test@hotmail.com", password="aassss")
        result = self.lp.verifyFailedLogin()
        assert result == True
