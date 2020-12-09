import time
import traceback
import random, string
import utilities.customlogger as cl
import logging

class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    # def getAlphaNumeric(self, length, type='letters'):
    def verifyTextContains(self, actualText, expectedText):
        self.log.info("Actual text : " + actualText)
        self.log.info("Expected text : "+ expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CORRECT")
            return True
        else:
            self.log.info("### VERIFICATION INCORRECT")
            return False

