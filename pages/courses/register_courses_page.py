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

    #Locators

    _search_field = "search" # id
    _course_link = "//h4[contains(text(),'Learn Python 3 from scratch')]//parent::div//parent::a" #xpath
    _enroll_link = "//button[contains(text(),'Enroll in Course')]" # xpath
    _creditcard_field = "cardnumber" # name inside frame 1
    _expdate_field = "exp-date" # name inside frame 2
    _cvc_field = "cvc" # name inside frame 3
    _buy_button = "//div[@class='stripe-outer ']//button" # xpath 3rd number
