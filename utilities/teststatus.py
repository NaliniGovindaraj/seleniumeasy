
import utilities.custom_logger as cl
import logging
from base.seleniumdriver import SeleniumDriver


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(10)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result is True:
                    self.resultList.append("PASS")
                    self.log.error("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage)

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):


        self.setResult(result,resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + "###Failed###")
            #print(self.resultList)
            self.resultList.clear()
            assert True == False

        else:
            self.log.error(testName + "###PASS###")
            #print(self.resultList)
            self.resultList.clear()
            assert True == True

