# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:43:34 2021

@author: Gebruiker
"""

"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

#I assume we can get negative numbers
l_number = [19, 15, 3, 7, -25, 42]
target = 17
complements = []

def list_check(list_of_numbers: list, target: int) -> bool:
    #check for each number in the list
    for i in l_number:
        x = target - i
        if i in complements:
            return True
            break
        else:
            complements.append(x)
    else:
        return False
    
print(list_check(l_number, 17))


