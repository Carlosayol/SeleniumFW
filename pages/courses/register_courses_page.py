# Esta clase hereda base_page
# Tener Locators para los diferentes cosas que vamos a escribir,
#   textbox, clicks y demas
# Escribir metodos que hagan las acciones
# Ejm: Seleccionar curso, entrar datos de la tarjeta de credito,
#   click en enrroll, metodos por separado para entrar los datos de las tarjetas,
#   macro metodos que llamen metodos mas pequeños
#   (como enroll course haga el scroll, click y entrar datos)
#   (verificar el error del mensaje mostrado (el mensaje se demora un poco en aparecer))
# Crear una test class

from base.base_page import BasePage
import time

class RegisterCoursesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _search_field = "search" # id
    _search_button = "//button[@class='find-course search-course']" #xpath
    _course_link = "//h4[contains(text(),'Learn Python 3 from scratch')]//parent::div//parent::a" #xpath
    _enroll_link = "//button[contains(text(),'Enroll in Course')]" # xpath
    _creditcard_field = "cardnumber" # name inside frame 1
    _expdate_field = "exp-date" # name inside frame 2
    _cvc_field = "cvc" # name inside frame 3
    _submit_button = "//div[@class='stripe-outer ']//button" # xpath 3rd number
    _enroll_error_message = "//span[contains(text(),'El número de tarjeta')]" # xpath

    # Methods

    def enterCourseName(self, course):
        self.sendElementKeys(self._search_field, course)

    def searchCourse(self):
        self.elementClick(self._search_button, locatorType="XPATH")

    # Selecting which course to enroll

    def selectCourseToEnroll(self):
        self.elementClick(self._course_link, locatorType="XPATH")

    # Enroll inside course page

    def clickEnrollButton(self):
        self.elementClick(self._enroll_link, locatorType="XPATH")

    # Info Card Methods

    def enterCreditCard(self, num):
        self.sendElementKeys(self._creditcard_field, num, locatorType="NAME")

    def enterExpDateCard(self, exp):
        self.sendElementKeys(self._expdate_field, exp, locatorType="NAME")

    def enterCVCCard(self, cvc):
        self.sendElementKeys(self._cvc_field, cvc, locatorType="NAME")

    # Enroll with complete info

    def clickSubmitButton(self):
        self.elementClick(self._submit_button, locatorType="XPATH")

    ### Bigger Methods

    def enterCreditCardInfo(self, num, exp, cvc):
        self.enterCreditCard(self, num)
        self.enterExpDateCard(self, exp)
        self.enterCVCCard(self, cvc)

    def enrollCourse(self, num="", exp="", cvc=""):
        self.clickEnrollButton(self)
        self.scrollBroswer(self, direction="down")
        self.enterCreditCardInfo(self, num, exp, cvc)
        self.clickSubmitButton(self)

