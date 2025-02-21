#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:02:41 2025

@author: madihamalik
"""

print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low + high) // 2

while True:
    print("Is your secret number " + str(guess) + "?")
    print("Enter 'h' to indicate the guess is too high.", end=' ')
    print("Enter 'l' to indicate the guess is too low.", end=' ')
    print("Enter 'c' to indicate I guessed correctly.", end=' ')

    ans = input()

    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess 
    elif ans == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.\n")
        continue

    guess = (low + high) // 2