#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 22:01:23 2025

@author: madihamalik
"""

def most_frequent_word(text):
    """
    Finds the most frequently occurring word in a given text.

    Args:
        text (str): A string containing words separated by spaces.

    Returns:
        str: The word that appears most frequently.

    Example:
        >>> most_frequent_word("apple banana apple orange banana apple")
        "apple"
    """
    words = text.split()
    freq_dict = {}

    # Count occurrences of each word
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1


    # Find the word with the highest frequency
    max_word = ""
    max_count = 0
    for word, count in freq_dict.items():
        if count > max_count:
        
            max_word = word
            max_count = count


        

    return max_word

print(most_frequent_word("orange apple banana orange apple  banana apple orange apple orange"))