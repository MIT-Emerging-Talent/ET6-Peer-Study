#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:35:16 2025

@author: madihamalik
"""

def get_data(aTuple):
3	    nums = ()
4	    words = ()
5	    for t in aTuple:
6	        nums = nums + (t[0],)   
7	        if t[1] not in words:   
8	            words = words + (t[1],)
9	    min_nums = min(nums)
10	    max_nums = max(nums)
11	    unique_words = len(words)
12	    return (min_nums, max_nums, unique_words)
13	
14	
15	(small, large, words) = get_data(((1, 'mine'), 
16	                                  (3, 'yours'),
17	                                  (5, 'ours'),
18	                                  (7, 'mine')))
