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

    @data(("5", "12", "17"))
    @unpack
    def test_valid_addition_TC1(self,value1,value2,expectedResult):
        self.mp.lightboxpop_close()
        self.mp.getTotal(value1,value2)
        actual_result = self.rv.getactualresult()
        print(actual_result)
        print(expectedResult)

        try:
            assert actual_result == expectedResult
            result1 = True
            self.ts.markFinal("test_valid_addition_TC1", result1, "TC1 Completed")
        except:
            result1 = False
            self.ts.markFinal("test_valid_addition_TC1", result1, "TC1 Completed")


    @pytest.mark.run(order=2)
    @data(("-5", "-6", "-11"),("a","b","NaN"))
    @unpack
    def test_valid_addition_TC2(self,value1,value2,expectedResult):
        self.mp.except_first_testcase()
        self.mp.getTotal(value1, value2)
        actual_result = self.rv.getactualresult()
        print(actual_result)
        print(expectedResult)
        try:
            assert actual_result == expectedResult
            result1 = True

            self.ts.markFinal("test_valid_addition_TC1", result1, "TC1 Completed")
        except:
            result1 = False
            self.ts.markFinal("test_valid_addition_TC1", result1, "TC1 Completed")

