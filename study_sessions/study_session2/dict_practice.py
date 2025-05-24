#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:08:49 2025

@author: madihamalik
"""


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')



def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    all_values = aDict.values()
    result = 0
    for val in all_values:
        result += len(val)

    
    return result



#print(how_many(animals))


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    
    in this case it should return d because d has the largest num of values which is 3
    
    animals['d'] = ['donkey', 'dog', 'dingo']
    '''
    # Your Code Here
    if len(aDict) == 0:
        return None
    
    count = {}
    
    for key in aDict:
        count[len(aDict[key])] = key
    return count[max(count)]
print(biggest(animals))