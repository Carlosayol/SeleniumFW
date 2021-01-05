# Hacer cosas similares a lo que esta en la otra clase de tests
# Usar fixtures
# Crear 1 metodo que haga:
#       ingresar nombre del curso
#       seleccionarlo
#       entrar al curso y aplicar al curso
#       verificar el mensaje de error
#       test status.markfinal

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

#   @pytest.mark.run(order=1)
#   def test_invalidEnroll(self):
#       self.courses.