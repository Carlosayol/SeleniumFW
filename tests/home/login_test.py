from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest():

    def test_validLogin(self):
        baseUrl = "https://courses.letskodeit.com"
        driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        loginLink = driver.find_element(By.XPATH,"//a[contains(text(),'Sign In')]")
        loginLink.click()

        emailForm = driver.find_element(By.ID,"email")
        emailForm.send_keys("test@email.com")

        passForm = driver.find_element(By.ID,"password")
        passForm.send_keys("abcabc")

        loginButton = driver.find_element(By.XPATH,"//input[@value='Login']")
        loginButton.click()

        searchBar = driver.find_element(By.XPATH,"//input[@id='search']")
        if searchBar is not None:
            print("Se ha ingresado correctamente")
        else:
            print("Error en el ingreso")

ff = LoginTest()
ff.test_validLogin()


