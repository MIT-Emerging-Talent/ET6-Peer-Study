#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 21:09:25 2025

@author: madihamalik
"""

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9 
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150

"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # if len(nums) == 2:
    #     return [0, 1]
    num_dict = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in num_dict:
            return [num_dict[diff], i]
        else:
            num_dict[num] = i
    return []


print(twoSum([0, 4, 3, 0], 0))
print(twoSum([3, 4], 6))  # Output: (0, 1)
print(twoSum([3, 2, 6], 6))
print(twoSum([0, 4, 3, 4, 0], 0))  # Output: (0, 4)
