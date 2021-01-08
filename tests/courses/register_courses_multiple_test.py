
# Comando tocho py.test -s -v test/courses/register_courses_test.py --browser chrome

from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
import unittest
import pytest

@pytest.mark.usefixtures("ModulesetUp","setUp")
@ddt
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, ModulesetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("Learn Python 3 from scratch","1231 2311 1131 1114","1224","111"),("JavaScript for beginners","1231 2311 1131 1114","1224","111"))
    @unpack
    def test_invalidEnroll(self, courseName, ccNum, ccExp, ccCVC):
        self.courses.enrollCourse(coursename=courseName, num=ccNum,exp=ccExp,cvc=ccCVC)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnroll",result,"Enroll verification")
        self.driver.find_element_by_xpath("//a[contains(text(),'ALL COURSES')]").click()