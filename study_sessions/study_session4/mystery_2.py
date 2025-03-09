#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

a = ""
while a.lower() != "frog":
    a = input("Please enter a frog: ")

    if a == "":
        print("You entered nothing, try again.")
    elif a.lower() != "frog":
        print('"' + a + '" is not  a frog, try again.')

print("thank you for the frog")
