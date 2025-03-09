#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Behavior: unit tests, documentation, function name, type hints
2. Implementation: comment what each line of code does (predictive stepping!)
3. Strategy pt. 1 - purpose: comment why each line of code exists
4. Strategy pt. 2 - connections: describe how different lines interact
5. strategy pt. 3 - goals: summarize the strategy using sub-goals
"""

"""
This is a simple program that takes a string from the user and print the reverse of it

input: a string to reverse
output: string the reverse version of the input string

user_input = 'Karim'
reversed_input = miraK

user_input = 'Aseel'
reversed_input = 'leesA'

user_input = 'Amro'
reversed_input = 'ormA'

"""

user_input = ""

# Ask for user input as long as they don't enter anything
while user_input == "":
    user_input = input("Enter some text to reverse: ")
    if user_input == "":
        print("nope, you have to enter something")

reversed_input = ""

# Iterate through the user_input and reverse it
for char in user_input:
    reversed_input = char + reversed_input


print("here is your reversed input: " + reversed_input)


assert reversed_input == "mirak", "Test 1"
