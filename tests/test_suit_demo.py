import unittest
from tests.courses.register_courses_csv_test import RegisterCoursesCSVTest
from tests.courses.register_courses_test import RegisterCoursesTest

# Get all test from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTest)

# Test suite
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)