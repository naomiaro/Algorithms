'''
Created on Nov 3, 2012

@author: naomiaro
'''
import unittest
import math
import ClosestPair as cp


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testEclideanDistance(self):
        p = (3, 4)
        q = (5, 6)
        a = math.sqrt(8)
        d = cp.euclideanDistance(p, q)
        self.assertEqual(d, a)
        
    def testFindClosestPair(self):
        P = [(1,1), (3,3), (4,6), (3,5), (4, 3.5)]
        pair = cp.findClosestPair(P)
        
        self.assertTrue((3,3) in pair)
        self.assertTrue((4, 3.5) in pair)
          
    def testClosestSplitPair(self):
        P = [(1,1), (3,3), (11,5), (45,47), (4,6), (3,5), (4, 3.5), (65, 3), (33, 22), (3, 7), (3, 11), (4, 14), (4, 4), (4, 16)]
        Px = sorted(P, key=lambda tup: tup[0])
        Py = sorted(P, key=lambda tup: tup[1])
    
        pair = cp.closestSplitPair(Px, Py, 2)
        
        self.assertTrue((4,4) in pair)
        self.assertTrue((4, 3.5) in pair)
        
    def testClosestPairSplit(self):
        P = [(1,1), (3,3), (11,5), (45,47), (4,6), (3,5), (4, 3.5), (65, 3), (33, 22), (3, 7), (3, 11), (4, 14), (4, 4), (4, 16)]
        Px = sorted(P, key=lambda tup: tup[0])
        Py = sorted(P, key=lambda tup: tup[1])
    
        pair = cp.closestPair(Px, Py)
        
        self.assertTrue((4,4) in pair)
        self.assertTrue((4, 3.5) in pair)
    
    def testClosestPairLeft(self):
        P = [(4, 3.5), (1,1), (3,3), (11,5), (4, 4), (45,47), (4,6), (3,5), (65, 3), (33, 22), (3, 7), (3, 11), (4, 14), (4, 16)]
        Px = sorted(P, key=lambda tup: tup[0])
        Py = sorted(P, key=lambda tup: tup[1])
    
        pair = cp.closestPair(Px, Py)
        
        self.assertTrue((4,4) in pair)
        self.assertTrue((4, 3.5) in pair)
        
    def testClosestPairRight(self):
        P = [(1,1), (3,3), (11,5), (45,47), (4,6), (3,5), (65, 3), (33, 22), (3, 7), (3, 11), (4, 14), (4, 4), (4, 16), (4, 3.5)]
        Px = sorted(P, key=lambda tup: tup[0])
        Py = sorted(P, key=lambda tup: tup[1])
    
        pair = cp.closestPair(Px, Py)
        
        self.assertTrue((4,4) in pair)
        self.assertTrue((4, 3.5) in pair)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()