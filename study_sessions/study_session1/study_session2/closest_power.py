#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:16:18 2025

@author: madihamalik
"""


import unittest

def closest_power(base, num):
    '''
    Finds the exponent such that base^exp is closest to num.
    
    Args:
        base (int): An integer greater than 1.
        num (int): An integer greater than 0.

    Returns:
        int: The exponent that gives the closest power of the base to num.
    '''
    # Define variables
    exp = 0
    
    # Iterate to find the closest exponent
    dif1 = abs(base**exp - num)
    dif2 = abs(base**(exp - 1) - num)
    
    while base**exp < num:
        exp += 1
        dif1 = abs(base**exp - num)
        dif2 = abs(base**(exp - 1) - num)
        
    if dif1 >= dif2:
        return exp - 1
    else:
        return exp


class TestClosestPower(unittest.TestCase):
    
    def test_exact_power(self):
        """Test when num is exactly a power of base"""
        self.assertEqual(closest_power(3, 9), 2)
        self.assertEqual(closest_power(4, 16), 2)
        self.assertEqual(closest_power(5, 125), 3)

    def test_closest_lower_power(self):
        """Test when num is closer to the lower power"""
        self.assertEqual(closest_power(3, 10), 2)  # 3^2 = 9, 3^3 = 27, closer to 9
        self.assertEqual(closest_power(4, 12), 2)  # 4^2 = 16, 4^1 = 4, closer to 16

    def test_closest_higher_power(self):
        """Test when num is closer to the higher power"""
        self.assertEqual(closest_power(3, 15), 2)  # 3^2 = 9, 3^3 = 27, closer to 9
        self.assertEqual(closest_power(2, 7), 3)   # 2^2 = 4, 2^3 = 8, closer to 8

    def test_small_numbers(self):
        """Test with small values for base and num"""
        self.assertEqual(closest_power(2, 1), 0)  # 2^0 = 1
        self.assertEqual(closest_power(2, 2), 1)  # 2^1 = 2

    def test_large_numbers(self):
        """Test with large base and num"""
        self.assertEqual(closest_power(10, 1000), 3)  # 10^3 = 1000
        self.assertEqual(closest_power(5, 200), 3)   # 5^3 = 125, 5^4 = 625, closer to 125

    def test_edge_cases(self):
        """Test with edge cases"""
        self.assertEqual(closest_power(3, 3), 1)  # 3^1 = 3
        self.assertEqual(closest_power(4, 5), 1)  # 4^1 = 4, 4^2 = 16, closer to 4
        self.assertEqual(closest_power(7, 50), 2) # 7^2 = 49, 7^3 = 343, closer to 49

if __name__ == '__main__':
    unittest.main()