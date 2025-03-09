#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

a = ""
while "cat" not in a.lower():
    a = input('Please enter something containing "cat": ')

    if a == "":
        print("You entered nothing, try again.")
    elif "cat" not in a.lower():
        print('"' + a + '" does not contain cat, try again.')

print("thank you for the cat")

assert a == "you are a cat", "Test 1"
