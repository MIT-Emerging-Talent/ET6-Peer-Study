#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:17:49 2025

@author: madihamalik
"""

"""
Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. 
You are also given a function f, that takes in two integers, performs an unknown operation 
on them, and returns a value.

Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). 
The function will return a tuple of two dictionaries: a dictionary of the intersection of d1 
and d2 and a dictionary of the difference of d1 and d2, calculated as follows:

Intersect:
- The keys to the intersect dictionary are keys that are common in both d1 and d2.
- To get the values of the intersect dictionary, look at the common keys in d1 and d2 and 
  apply the function f to these keys' values. 
- The value of the common key in d1 is the first parameter to the function, and the value of 
  the common key in d2 is the second parameter to the function.
- Do not implement f inside your dict_interdiff code -- assume it is defined outside.

Difference:
- A key-value pair in the difference dictionary is:
  (a) Every key-value pair in d1 whose key appears only in d1 and not in d2.
  (b) Every key-value pair in d2 whose key appears only in d2 and not in d1.

Examples:

If f(a, b) returns a + b:
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

Intersect{1: 70, 2: 70, 3: 90}

Difference{5: 80, 4: 70, 6: 90}

then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

If f(a, b) returns a > b:
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
"""
#*************************************************************************************************************
"""
Created on Wed Feb 19 13:38:16 2025

@author: somai
"""
#Problem 3
# Instructions:
# 1. Define a function dict_interdiff(d1, d2) that takes two dictionaries as input.
# 2. Create two empty dictionaries:
#    - intersect (to store common keys with function f applied).
#    - difference (to store keys unique to either d1 or d2).
# 3. Extract the keys of d1 and d2 for comparison.
# 4. Iterate through keys in d1:
#    - If the key exists in both d1 and d2, apply f to their values and store it in intersect.
#    - If the key only exists in d1, add it to difference.
# 5. Iterate through keys in d2:
#    - If the key only exists in d2, add it to difference.
# 6. Return a tuple of the two dictionaries: (intersect, difference).


import unittest
def dict_interdiff(d1, d2):

    
    # Declare empty dictionaries for intersection and difference
    Intersect = {}
    Difference = {}
    
    # Get keys from both dictionaries
    d1_key = d1.keys()
    d2_key = d2.keys()
    print( d1_key)
    print(d2_key)

    # Compute intersection (apply function f to common keys)
    for key in d1_key:
        if key in d2_key:
            value = f(d1[key], d2[key])
            Intersect[key] = value
        else:
            Difference[key] = d1[key]

    # Compute difference (keys in d1 but not in d2)


    # Compute difference (keys in d2 but not in d1)
    for key in d2_key:
        if key not in d1_key:
            Difference[key] = d2[key]
    return (Intersect, Difference)
    
    
def f(a, b):
    return a > b
d1 = {1: 30, 2: 20, 3: 30, 5: 80}
d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}
    
    
    
print(dict_interdiff(d1, d2))
    
class TestDictInterdiff(unittest.TestCase):

    def test_basic_addition(self):
        """Test with addition as function f"""

        d1 = {1:30, 2:20, 3:30}
        d2 = {1:40, 2:50, 3:60}

            
        expected_output = ({1: False, 2: False, 3: False}, {})
        self.assertEqual(dict_interdiff(d1, d2), expected_output)

if __name__ == '__main__':
    unittest.main()
