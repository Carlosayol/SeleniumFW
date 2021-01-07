
# Comando tocho py.test -s -v test/courses/register_courses_test.py --browser chrome

from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("ModulesetUp","setUp")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, ModulesetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnroll(self):
        self.courses.enrollCourse(coursename="Learn Python 3 from scratch", num="1231 2311 1131 1114",exp="1224",cvc="111")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnroll",result,"Enroll verification")