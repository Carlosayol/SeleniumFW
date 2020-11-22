from selenium import webdriver

class WebDriverFactor():

    def __init__(self,browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl = "https://courses.letskodeit.com"
        if self.browser == "chrome":
            driver = webdriver.Chrome()
            print("Running test on Chrome")
        else:
            driver = webdriver.Chrome()
            print("Running test on Mew")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        return driver

