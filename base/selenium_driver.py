from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utilities.customlogger as cl


class SeleniumDriver():

    log = cl.customLogger(logLevel=logging.DEBUG)

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
            self.log.info("Locator type is not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found")
        except:
            self.log.info("Element not found")
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Element has been clicked")
        except:
            self.log.info("Cannot click the element")
            print_stack()

    def sendElementKeys(self, locator, data,locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Keys has been send")
        except:
            self.log.info("Cannot send keys")
            print_stack()

    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                self.log.info("Element found")
                return True
            else: return False
        except:
            self.log.info("Element not found")
            return False

    def ElementsPresent(self, locator, byType):
        try:
            elements = self.driver.find_elements(byType, locator)
            if len(elements)>0:
                self.log.info("Element found")
                return True
            else: return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",timeout=10,
                       pollFrequency=0.5):

        element = None
        try:
            byType = self.hw.getByType(locatorType)
            self.log.info("Esperando a :: " +str(timeout)+ " :: segundos para que aparezca el elemento")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            element.click()
            self.log.info("Elemento aparecio en la web")
        except:
            self.log.info("No aparecio el elemento")
            print_stack()
        return element