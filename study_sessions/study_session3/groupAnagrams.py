#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 21:04:06 2025

@author: madihamalik
"""

"""
Given a list of words, group together all words that are anagrams of each other. An anagram is a word formed 
by rearranging the letters of another word. The order of groups in the output does not matter.

Examples:

Example 1:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Explanation:
	•	“bat” has no anagram in the list.
	•	“nat” and “tan” are anagrams of each other.
	•	“ate”, “eat”, and “tea” are anagrams of each other.

Example 2:

Input: [""]
Output: [[""]]

Example 3:

Input: ["a"]
Output: [["a"]]

Constraints:
	•	1 ≤ strs.length ≤ 10⁴
	•	0 ≤ strs[i].length ≤ 100
	•	Each word contains only lowercase English letters.
    
https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

"""