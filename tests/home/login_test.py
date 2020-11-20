from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTest(unittest.TestCase):

    def test_validLogin(self):
        baseUrl = "https://courses.letskodeit.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        lp = LoginPage(driver)
        lp.login()

        searchBar = driver.find_element(By.XPATH,"//input[@id='search']")
        if searchBar is not None:
            print("Se ha ingresado correctamente")
        else:
            print("Error en el ingreso")

ff = LoginTest()
ff.test_validLogin()


