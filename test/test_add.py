from ddt import ddt,data,unpack
from utilities.result_verification import ResultVerification
from utilities.teststatus import TestStatus
from pages.mainpage import MainPage
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestAdd(unittest.TestCase):

    @pytest.fixture(autouse=True)

    def classSetup(self, oneTimeSetUp):
        self.mp = MainPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.rv = ResultVerification(self.driver)
        self.driver.implicitly_wait(10)

    @pytest.mark.run(order=1)

    @data(("-5", "12", "7"))
    @unpack
    def test_valid_addition_TC1(self,value1,value2,expectedResult):
        self.mp.lightboxpop_close()
        self.mp.getTotal(value1,value2)
        actual_result = self.rv.getactualresult()
        print(actual_result)
        print(expectedResult)
        if actual_result == expectedResult:
            result1 = True
            self.ts.markFinal("test_successful_login", result1, "TC1 Completed")
        else:
            result1 = False
            self.ts.markFinal("test_successful_login", result1, "TC1 Completed")



    @pytest.mark.run(order=2)
    @data(("5", "12", "17"),("a","b","NaN"))
    @unpack
    def test_valid_addition_TC2(self,value1,value2,expectedResult):
        self.mp.except_first_testcase()
        self.mp.getTotal(value1, value2)
        actual_result = self.rv.getactualresult()
        if actual_result == expectedResult:
            result1 = True
            self.ts.markFinal("test_successful_login", result1, "TC2 Completed")
        else:
            result1 = False
            self.ts.markFinal("test_successful_login", result1, "TC2 Completed")

