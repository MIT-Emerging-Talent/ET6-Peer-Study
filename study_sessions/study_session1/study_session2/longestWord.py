#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:51:04 2025

@author: madihamalik
"""
import unittest
"""
Given an array of strings words representing an English Dictionary, r
eturn the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. 
If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character 
being added to the end of a previous word. 

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
"""

def longestWord(words):
    """
    :type words input: List[str] of integers 
    :return type: a string of the longest word in the list
    
    longestWord(['K', 'Ka', 'Kar', 'Kari', 'Karim'])
    Karim
    
    longestWord(["a","banana","app","appl","ap","apply","apple"])
    apple
    
    longestWord([])
    ValueError
    """
    
    # take the last element from the list
    longest = ''
    accepted_words = []
    # iterate through the loop
    for word in words:
        temp_list = []
        for i in range(0, len(word)- 1):
            temp_list.append(word[:i+1])
        can_be_contructed = True
        for item in temp_list:
            if item not in words:
                can_be_contructed = False
        if can_be_contructed :
            accepted_words.append(word)

    for word in accepted_words:
        if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
            longest = word
        


    return longest




print(longestWord(["a","banana","app","appl","ap","apply","apple"]))











        