
from pages.courses.register_courses_page import RegisterCoursesPage
from pages.navigation.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import unittest
import pytest

@pytest.mark.usefixtures("ModulesetUp","setUp")
@ddt
class RegisterCoursesCSVTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, ModulesetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateAllCoursesLink()

    @pytest.mark.run(order=1)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_invalidEnroll(self, courseName, ccNum, ccExp, ccCVC):
        self.courses.enrollCourse(coursename=courseName, num=ccNum,exp=ccExp,cvc=ccCVC)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnroll",result,"Enroll verification")