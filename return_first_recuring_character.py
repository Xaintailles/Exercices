# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:57:31 2021

@author: Calixte Allier
"""

"""
Return the first recuring character in an array
eg:
    [A,B,C,A] --> A
    [B,C,A,B,A] --> B
    [A,B,C] --> null
"""

from collections import Counter

l_strings = ['A','B','C','A']
l_strings = ['B','C','A','B','A']
l_strings = ['A','B','C']

def return_first_repeating(list_of_strings: list) -> str:

    c = Counter(list_of_strings)
    
    for item, value in c.items():
        if value > 1:
            return(item)
            break
    
    else:
        pass
    
print(return_first_repeating(l_strings))

"""
This solution should be O(n) for Counter and O(n) for iterating through the dictionnary
Maybe not the best optimized solution for time
"""
            