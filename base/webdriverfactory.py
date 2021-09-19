from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):

        baseUrl = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        return driver

