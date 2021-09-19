from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
from base.seleniumdriver import SeleniumDriver

class MainPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _input1_field = "sum1"
    _input2_field = "//input[@id ='sum2']"#xpath
    _gettotal_button = "//button[@ onclick='return total()']"#xpath
    _close_button = 'at-cv-lightbox-close'
    _header_text = "//div[@class = 'panel-heading' and contains(text(),'Two Input Fields')]"


    #actions
    def enterInput1(self,value1):
        self.sendKeys(value1,locator=self._input1_field,locatorType='id')

    def enterInput2(self, value2):
        self.sendKeys(value2, self._input2_field, locatorType='xpath')

    def clickGetTotal(self):
        self.elementClick(self._gettotal_button,locatorType='xpath')

    #method

    def lightboxpop_close(self):
        #time.sleep(4)
        element = self.driver.execute_script("return document.getElementById('at-cv-lightbox-close');")
        element.click()
        #time.sleep(4)
        self.webScroll(direction='down')
        self.waitForElement(self._header_text, locatorType='xpath', timeout=15, pollFrequency=1)
        self.waitForElement(self._input1_field, locatorType='id', timeout=14, pollFrequency=1)

    def except_first_testcase(self):
        self.driver.refresh()
        self.webScroll(direction='down')
        self.waitForElement(self._header_text, locatorType='xpath', timeout=15, pollFrequency=1)
        self.waitForElement(self._input1_field, locatorType='id', timeout=14, pollFrequency=1)

    def getTotal(self,value1,value2):
        self.enterInput1(value1)
        self.enterInput2(value2)
        self.clickGetTotal()
