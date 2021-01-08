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

    _search_field = "//input[@id='search']"  # id
    _search_button = "//button[@class='find-course search-course']"  # xpath
    _course_link = "//h4[contains(text(),'Learn Python 3 from scratch')]//parent::div//parent::a"  # xpath
    _enroll_link = "//button[contains(text(),'Enroll in Course')]"  # xpath
    _creditcard_field = "cardnumber"  # name inside frame 1
    _expdate_field = "exp-date"  # name inside frame
    _cvc_field = "cvc"  # name inside frame 2
    _submit_button = "//div[@class='stripe-outer ']//button"  # xpath 3rd number
    _enroll_error_message = "//span[contains(text(),'El número de tu tarjeta')]"  # xpath

    # Methods

    def enterCourseName(self, course):
        self.sendElementKeys(self._search_field, course,locatorType="XPATH")

    def clickSearchCourse(self):
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
        buttons = self.getElementList(self._submit_button,locatorType="XPATH")
        self.elementClick(element=buttons[2])

    ### Functionality

    def enterCreditCardInfo(self, num, exp, cvc):
        self.switchToFrame(0)
        self.enterCreditCard(num)
        self.switchToDefault()
        self.switchToFrame(1)
        self.enterExpDateCard(exp)
        self.switchToDefault()
        self.switchToFrame(2)
        self.enterCVCCard(cvc)
        self.switchToDefault()

    def enrollCourse(self, coursename="Learn Python 3 from scratch", num="", exp="", cvc=""):
        self.enterCourseName(coursename)
        self.clickSearchCourse()
        self.selectCourseToEnroll()
        self.clickEnrollButton()
        self.scrollBroswer(direction="down")
        self.enterCreditCardInfo(num, exp, cvc)
        self.clickSubmitButton()

    def verifyEnrollFailed(self):
        time.sleep(4)
        result = self.isElementDisplayed(self._enroll_error_message, locatorType="XPATH")
        return result
