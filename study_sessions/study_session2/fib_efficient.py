#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:27:25 2025

@author: madihamalik
fib = 1, 2, 3, 5, 8, 13, 21, 34
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
def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
        
        
numFibCalls = 0
fibArg = 34

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0
        
d = {1:1, 2:2}
print(fib_efficient(fibArg, d))
print('function calls', numFibCalls)
