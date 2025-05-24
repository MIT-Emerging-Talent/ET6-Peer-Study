#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:31:12 2025

@author: madihamalik
"""

# Write a function that satisfies the following docstring:

# def largest_odd_times(L):
#     """ Assumes L is a non-empty list of ints
#         Returns the largest element of L that occurs an odd number 
#         of times in L. If no such element exists, returns None """
#     # Your code here
# For example, if

# largest_odd_times([2,2,4,4]) returns None
# largest_odd_times([3,9,5,3,5,3]) returns 9
# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.
#****************************************************************************
"""
Instructions:
1. Define a function `largest_odd_times(L)` that takes a non-empty list of integers as input.
2. The function should find the largest number that appears an odd number of times in the list.
3. If no number appears an odd number of times, return `None`.

Implementation Steps:
- Iterate through the list and count occurrences of each element.
- Identify numbers that occur an odd number of times.
- Return the largest such number, or `None` if no odd-occurring number exists.
"""

import unittest

def largest_odd_times(L):
    """
    Finds the largest number in the list that appears an odd number of times.
    
    Args:
        L (list): A list of integers.

    Returns:
        int or None: The largest integer that appears an odd number of times, 
                     or None if no such number exists.
    """
    aDict = {}

    for num in L:
        if num in aDict:
            aDict[num] += 1
        else:
            aDict[num] = 1

    largestOddNum = None

    for key, values in aDict.items():
        if values % 2 == 1:  # Check if the occurrence count is odd
            if largestOddNum is None or key > largestOddNum:
                largestOddNum = key

    return largestOddNum


class TestLargestOddTimes(unittest.TestCase):
    
    
    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(largest_odd_times([]), None)
        
    def test_single_odd_occurrence(self):
        """Test with a list containing a single odd-occurring number"""
        self.assertEqual(largest_odd_times([2, 2, 3, 3, 3]), 3)

    def test_multiple_odd_occurrences(self):
        """Test with multiple odd-occurring numbers, ensuring the largest is chosen"""
        self.assertEqual(largest_odd_times([1, 1, 2, 2, 12, 12, 12, 12,12, 5, 5, 5]), 12)

    def test_no_odd_occurrences(self):
        """Test with a list where no number appears an odd number of times"""
        self.assertIsNone(largest_odd_times([2, 2, 4, 4, 6, 6]), None)

    def test_single_element_list(self):
        """Test with a single-element list"""
        self.assertEqual(largest_odd_times([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(largest_odd_times([]))

    def test_all_numbers_odd_occurrences(self):
        """Test with all numbers appearing an odd number of times"""
        self.assertEqual(largest_odd_times([1, 1, 1, 3, 3, 3, 5, 5, 5]), 5)

    def test_mixed_positive_and_negative_numbers(self):
        """Test with positive and negative numbers"""
        self.assertEqual(largest_odd_times([-3, -3, -3, 2, 2, 2, 4, 4, -1, -1, -1]), 2)

    def test_large_numbers(self):
        """Test with large numbers to ensure function handles them correctly"""
        self.assertEqual(largest_odd_times([1000000, 1000000, 1000001]), 1000001)

if __name__ == '__main__':
    unittest.main()