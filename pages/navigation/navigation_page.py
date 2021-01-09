from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators all xpath

    _home_link = "//a[contains(text(),'HOME')]"
    _allcourses_link = "//a[contains(text(),'ALL COURSES')]"
    _support_link = "//a[contains(text(),'SUPPORT')]"
    _mycourses_link = "//a[contains(text(),'MY COURSES')]"

    # Acciones

    def navigateHomeLink(self):
        self.elementClick(self._home_link, locatorType="XPATH")

    def navigateAllCoursesLink(self):
        self.elementClick(self._allcourses_link, locatorType="XPATH")

    def navigateSupportLink(self):
        self.elementClick(self._support_link, locatorType="XPATH")

    def navigateMyCoursesLink(self):
        self.elementClick(self._mycourses_link, locatorType="XPATH")
