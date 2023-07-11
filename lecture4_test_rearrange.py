#!/usr/bin/env python3

from lecture4_test import rearrange_name
import unnitest

class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = 'Lovelace, Ada'
		expected = 'Ada Lovelace'					
		self.assertEqual(rearrange_name(testcase), expected)
	
	def test_empty(self):   #edge case 1 - empty value
		testcase = ''
		expected = ''
		self.assertEqual(rearrage_name(testcase), expected)
		
	def test_double_name(self):
		testcase = "Hopper, Grace M."
		expected = "Grace M. Hopper"
		self.assertEqual(rearrange_name(testcase), expected)
		
	def test_one_name(self): #edge case 2 - one value
		testcase = "Voltaire"
		expected = "Voltaire"
		self.assertEqual(rearrange_name(testcase), expected)
		
		
		

unittesst.main()
