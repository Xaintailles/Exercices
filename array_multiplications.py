# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:38:35 2021

@author: Gebruiker
"""

"""
Given an array of integers, return a new array such that each element at index 
i of the new array is the product of all the numbers in the original 
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

import numpy as np

l_example = [1, 2, 3, 4, 5]


def return_computed_product(l_input: list) -> list:
    
    if len(l_input) == 0:
        return('Please provide valid list')
    
    #We create an array that holds the same number of elements as the input
    #and is the result of the multiplication of every member of the array

    l_total_product = [np.product(l_input)] * len(l_input)
    l_total_product = np.array(l_total_product)
    
    l_input = np.array(l_input)
    
    #Then we can just divide both arrays and that will give the correct result
    
    l_return = l_total_product / l_example
    l_return = l_return.astype(int)
    
    return l_return

print(return_computed_product(l_example))

#Solving the follow-up brute-force style, not really ideal

def return_computed_product_without_division(l_input: list) -> list:
    
    if len(l_input) == 0:
        return('Please provide valid list')
    
    l_return = []
    
    for i in range(len(l_example)):
        #Need to initiate a new list, had difficulties there XD
        new_list = list(l_example)
        del new_list[i]
        l_return.append(np.product(new_list))
        
    return l_return
    
print(return_computed_product_without_division(l_example))
    

