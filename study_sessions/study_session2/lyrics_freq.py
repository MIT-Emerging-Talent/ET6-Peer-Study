#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:20:20 2025

@author: madihamalik
"""

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict
    
blinding_lights = [
    'Yeah', "I've", 'been', 'tryna', 'call', "I've", 'been', 'on', 'my', 'own', 
    'for', 'long', 'enough', 'Maybe', 'you', 'can', 'show', 'me', 'how', 'to', 
    'love,', 'maybe', "I'm", 'going', 'through', 'withdrawals', 'You', "don't", 
    'even', 'have', 'to', 'do', 'too', 'much', 'You', 'can', 'turn', 'me', 'on', 
    'with', 'just', 'a', 'touch,', 'baby', 'I', 'look', 'around', 'and', 'Sin', 
    "City's", 'cold', 'and', 'empty', '(oh)', 'No', "one's", 'around', 'to', 'judge', 
    'me', '(oh)', 'I', "can't", 'see', 'clearly', 'when', "you're", 'gone', 'I', 
    'said,', 'ooh,', "I'm", 'blinded', 'by', 'the', 'lights', 'No,', 'I', "can't", 
    'sleep', 'until', 'I', 'feel', 'your', 'touch', 'I', 'said,', 'ooh,', "I'm", 
    'drowning', 'in', 'the', 'night', 'Oh,', 'when', "I'm", 'like', 'this,', "you're", 
    'the', 'one', 'I', 'trust', '(Hey,', 'hey,', 'hey)', "I'm", 'running', 'out', 
    'of', 'time', "'Cause", 'I', 'can', 'see', 'the', 'sun', 'light', 'up', 'the', 
    'sky', 'So', 'I', 'hit', 'the', 'road', 'in', 'overdrive,', 'baby,', 'oh', 'The', 
    "city's", 'cold', 'and', 'empty', '(oh)', 'No', "one's", 'around', 'to', 'judge', 
    'me', '(oh)', 'I', "can't", 'see', 'clearly', 'when', "you're", 'gone', 'I', 
    'said,', 'ooh,', "I'm", 'blinded', 'by', 'the', 'lights', 'No,', 'I', "can't", 
    'sleep', 'until', 'I', 'feel', 'your', 'touch', 'I', 'said,', 'ooh,', "I'm", 
    'drowning', 'in', 'the', 'night', 'Oh,', 'when', "I'm", 'like', 'this,', "you're", 
    'the', 'one', 'I', 'trust', "I'm", 'just', 'walking', 'by', 'to', 'let', 'you', 
    'know', '(by', 'to', 'let', 'you', 'know)', 'I', 'can', 'never', 'say', 'it', 
    'on', 'the', 'phone', '(say', 'it', 'on', 'the', 'phone)', 'Will', 'never', 'let', 
    'you', 'go', 'this', 'time', '(ooh)', 'I', 'said,', 'ooh,', "I'm", 'blinded', 
    'by', 'the', 'lights', 'No,', 'I', "can't", 'sleep', 'until', 'I', 'feel', 'your', 
    'touch', '(Hey,', 'hey,', 'hey)', '(Hey,', 'hey,', 'hey)', 'I', 'said,', 'ooh,', 
    "I'm", 'blinded', 'by', 'the', 'lights', 'No,', 'I', "can't", 'sleep', 'until', 
    'I', 'feel', 'your', 'touch'
]

#print(lyrics_to_frequencies(blinding_lights))

weeknd = lyrics_to_frequencies(blinding_lights)

def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    
    words = []
    
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    
    return (words, best)

#print(most_common_words(weeknd))


def words_often(freqs, minTimes):
    result = []
    
    done = False
    
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w]) #remove word from dictionary
        else:
            done = True
    return len(freqs.values())

#print(words_often(weeknd, 5))












