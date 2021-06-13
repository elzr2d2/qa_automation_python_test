import unittest
from testCases.test_login import Test_Login
from testCases.test_data_object import Test_Data_Object

# Get all tests from the test classes
testLoader = unittest.TestLoader()

sanity = [testLoader.loadTestsFromTestCase(Test_Login),
          testLoader.loadTestsFromTestCase(Test_Data_Object)]

# Create a test suite combining all test classes
unittest.TestSuite(sanity)
# regressionTest = unittest.TestSuite([tc2, tc1])
