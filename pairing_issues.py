# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:26:42 2021

@author: Gebruiker
"""

"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the 
first and last element of that pair. For example, car(cons(3, 4)) 
returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

test = cons(1,2)
