#!/usr/bin/python
# -*- coding: utf-8 -*-
​
import unittest
from insight import subset,find_year_and_product,match
​
​
class TestDemo(unittest.TestCase):
    """Test mathfuc.py"""
​
    @classmethod
    def setUpClass(cls):
        print ("this setupclass() method only called once.\n")
​
    @classmethod
    def tearDownClass(cls):
        print ("this teardownclass() method only called once too.\n")
​
    def setUp(self):
        print ("do something before test : prepare environment.\n")
​
    def tearDown(self):
        print ("do something after test : clean up.\n")
​
    def test_subset(self):
        #Test method subset(list)
        #Empty Set
        self.assertEqual([],subset([]))
        self.assertNotEqual([],subset([]))
​
    def test_find_year_and_product(self):
        #Test method subset(list)
        #Empty Set
        self.assertEqual([],find_year_and_product([]))
        self.assertNotEqual([],find_year_and_product([]))
        #Test only one record
        self.assertEqual(['Credit card', 2011],find_year_and_product([[2011, 'Credit card', 'BANK OF AMERICA, NATIONAL ASSOCIATION']]))
        self.assertNotEqual(['Credit card', 2011],find_year_and_product([[2011, 'Credit card', 'BANK OF AMERICA, NATIONAL ASSOCIATION']]))
        
    def test_match(self):
        #Test method match
        #Empty Set
        self.assertEqual([],match([],[]))
        self.assertNotEqual([],match([],[]))
        
​
​
if __name__ == '__main__':
    unittest.main(verbosity=1)
