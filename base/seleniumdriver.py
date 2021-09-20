from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def getByType(self, locatorType):
        """
        returns Bytype
        """

        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " is not correct")
        return False

    def getElement(self, locator, locatorType="id"):

        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Succesfully found element with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Unable to find Element with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):

        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Successfully clicked the element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Unable to click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Succssfully Sent data with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Unable to send data with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()


    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)

            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,locator)))

            self.log.info("Successfully Element appeared on the web page")
        except:
            self.log.info("Unable to find Element on the web page")
            print_stack()
        return element

    def webScroll(self, direction="up"):

        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 900);")

    def getText(self, locator="", locatorType="id"):

        try:
            element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) != 0:
                text = text.strip()

        except:
            self.log.error("Failed to get text on element ")
            print_stack()
            text = None
        return text

    def screenShot(self, resultMessage):

        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

