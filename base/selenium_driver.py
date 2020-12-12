from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utilities.customlogger as cl
import time
import os

class SeleniumDriver():

    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time()*1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFileName = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFileName)
            self.log.info("Screenshot saved at: ", destinationFileName)
        except:
            self.log.error("### Exception Ocurred")
            print_stack()


    def getTitle(self):
        return self.driver.title

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

    def getElementList(self, locator, locatorType="id"):
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Elements found")
        except:
            self.log.info("Elements not found")
        return elements


    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator: # Esto verifica si el locator no esta vacio
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

    def getText(self, locator="", locatorType="id", element= None ,info =""):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                text = text.strip()
            self.log.info("Text has been retrieved")
        except:
            self.log.error("Failed to get text on element")
            print_stack()
            text = None
        return text


    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
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

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element is not displayed")
            return isDisplayed
        except:
            self.log.info("No aparecio el elemento")
            return False

    def scrollBroswer(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0,-1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0,1000);")