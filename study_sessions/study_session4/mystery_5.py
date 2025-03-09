#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

# --- declare the helper function ---


def a(b: list) -> list:
    """Creates a reversed copy of a list"""
    c = []
    for d in b:
        c.insert(0, d)
    return c


# --- use the helper function in a program ---

e = []

f = None
while f != "":
    print("\nSaved e: ", e)
    f = input("Enter some text to add to the list, or enter nothing to finish: ")
    if f != "":
        e.append(f)

g = a(e)

print("\nHere are your list in reverse order: ", g)
