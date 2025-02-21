#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:03:42 2025

@author: madihamalik

Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic
"""
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b * x + c

