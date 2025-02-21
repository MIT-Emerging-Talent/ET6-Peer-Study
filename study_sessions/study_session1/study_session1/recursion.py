#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:37:13 2025

@author: madihamalik
"""

"""

Count the Number of Digits in a Positive Integer (Using Recursion)
Explanation:
When given a positive integer, the goal is to determine how many digits it contains. You can approach this problem using recursion—breaking it down into smaller parts until the problem becomes simple enough to solve directly. Think about how you can repeatedly reduce the number and count its digits until only one digit remains.

In recursion, you need to define:

A base case: When is the answer obvious?

A recursive call: How can you break the problem into a smaller version of itself?

Instructions:
Define a function that takes a positive integer as input and returns how many digits it contains.
Think about the simplest possible case: What is the number of digits in a single-digit number?
If the number is not a single-digit number, find a way to reduce it to a smaller number and count the digits in that smaller number.
Combine the result of the smaller problem with the current number to build the solution step by step.
Test your function with different numbers and observe how the function works for large values.

 Test Cases:
print(count_digits_recursive(5))        # Output: 1
print(count_digits_recursive(12345))    # Output: 5
print(count_digits_recursive(1000000))  # Output: 7


"""

def count_digits_recursive(digit):
    if digit <= 9:
        return 1
    
    
    
    return 1 + count_digits_recursive(digit // 10)


print(count_digits_recursive(1))
print(count_digits_recursive(12345))
print(count_digits_recursive(1000000)) 

