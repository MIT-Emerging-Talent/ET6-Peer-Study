#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This function takes a string and returns the reverse of it.

input: a string that we are going to reverse
output: the reverse of the input string


"""

# --- declare the helper function ---


def reverse_string(user_input: str) -> str:
    """
    This function takes a string and returns the reverse of it.

    args:
      a string that we are going to reverse
    returns:
    the reverse of the input string

    >>> reverse_string('Aseel')
    'leesA'

    >>> reverse_string('Karim')
    'miraK'

    >>> reverse_string('Amro')
    'ormA'
    """
    reversed_input = ""
    # Iterate through the user_input and reverse it
    for char in user_input:
        reversed_input = char + reversed_input
    return reversed_input


assert reverse_string("") == "", "Test 0"
assert reverse_string("xyz") == "zyx", "Test 1"
assert reverse_string("Malayalam") == "malayalaM", "Test 2"
assert reverse_string("1729") == "9271", "Test 3"


# --- use the helper function in a program ---


user_input = ""
# Ask for user input as long as they don't enter anything
while user_input == "":
    user_input = input("\nEnter some something to reverse: ")
    if user_input == "":
        print("Nope, gotta enter something.  Try again.")

f = reverse_string(user_input)

print(user_input, " -> ", f)
