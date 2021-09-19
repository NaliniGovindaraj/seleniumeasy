from base.seleniumdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class ResultVerification(SeleniumDriver):

    log =cl.customLogger(logging.INFO)

    #locator

    _gettotal = "//span[@id ='displayvalue']"

    #method

    def getactualresult(self):
        actualResult = self.getText(locatorType='xpath',locator=self._gettotal)
        return actualResult


