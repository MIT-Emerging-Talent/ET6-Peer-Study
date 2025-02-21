#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:35:25 2025

@author: madihamalik
"""

"""
Bisection Search for a Threshold Value in a Numeric String
Explanation:
Bisection search is not just for characters—it can also help find values in ordered data.

Given a sorted string of numeric values, we can efficiently find the smallest number ≥ a given threshold.

Instead of checking every number one by one (O(n)), we use bisection search (O(log n)) to quickly narrow down the search space.

Instructions:
Create a variable sorted_numbers with the value "134789" (a sorted sequence of numeric characters).
Create a function find_threshold_bisection(sorted_nums, threshold) that searches for the smallest number ≥ threshold using bisection search.
Inside the function, define low as 0 (first index) and high as len(sorted_nums) - 1 (last index).
Use a while loop to repeatedly:
Find the middle index (mid = (low + high) // 2).
If sorted_nums[mid] >= threshold, store it as result and move left (high = mid - 1)` to find a smaller valid number.
Otherwise, move right (low = mid + 1).
If no valid number is found, return -1.
Call the function with sorted_numbers = "134789" and test with different thresholds ("5", "7", "2", "8").


we’re looking for the smallest number in the sorted string that is greater than or equal to this threshold.

For example:
	1.	Threshold: “5”
	•	In the string "134789", we want to find the smallest number that is greater than or equal to 5.
	•	The result is 7, because it is the smallest number that satisfies the condition.
	2.	Threshold: “3”
	•	In the string "2345679", we want the smallest number that is greater than or equal to 3.
	•	The result is 3, because 3 is the threshold itself.
	3.	Threshold: “8”
	•	In the string "2345679", there is no number greater than or equal to 8, so the result is -1.

#Test Cases:
print(find_threshold_bisection("134789", "5"))  # Output: 7  
print(find_threshold_bisection("2345679", "3"))  # Output: 3  
print(find_threshold_bisection("2345679", "8"))  # Output: -1  

"""

def find_threshold_bisection(sorted_nums, threshold):
    low = 0
    high = len(sorted_nums) - 1
    
    result = -1
    
    while low <= high:
        
        middle = (high + low )//2
        
        mid_number = sorted_nums[middle]
        
        if mid_number > threshold:
            result = mid_number
            high = middle -1
            
            
        elif mid_number == threshold:
            return mid_number
        
        elif mid_number < threshold:
            low = middle + 1

    if result != -1:
        return result
    else:
        return -1
    

        
print(find_threshold_bisection("134789", "5"))



print(find_threshold_bisection("2345679", "3"))
print(find_threshold_bisection("2345673", "8"))