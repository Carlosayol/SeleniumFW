from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "name":
            return By.NAME
        else:
            print("Locator type is not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found")
        except:
            print("Element not found")
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Element has been clicked")
        except:
            print("Cannot click the element")
            print_stack()

    def sendElementKeys(self, locator, data,locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Keys has been send")
        except:
            print("Cannot send keys")
            print_stack()

    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element found")
                return True
            else: return False
        except:
            print("Element not found")
            return False

    def ElementsPresent(self, locator, byType):
        try:
            elements = self.driver.find_elements(byType, locator)
            if len(elements)>0:
                print("Element found")
                return True
            else: return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",timeout=10,
                       pollFrequency=0.5):

        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Esperando a :: " +str(timeout)+ " :: segundos para que aparezca el elemento")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            element.click()
            print("Elemento aparecio en la web")
        except:
            print("No aparecio el elemento")
            print_stack()
        return element