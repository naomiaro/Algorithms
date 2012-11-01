'''
Created on Oct 31, 2012

@author: naomiaro
'''
import unittest
import MergeSortWithInversions as mswi

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testInversions(self):
        v = [6, 5, 4, 3, 2, 1]
        output, inv = mswi.mergesort(v)
        self.assertEqual(inv, 15)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()