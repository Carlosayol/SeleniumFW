from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utilities.customlogger as cl

class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.info("### EXCEPTION FAIL ")


    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        print()

