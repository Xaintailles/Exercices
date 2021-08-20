# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:33:34 2021

@author: Gebruiker
"""

"""
Given an integer k and a string s, find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k 
distinct characters is "bcb".
"""

k = 5

string = 'abcbadef'

### 

def get_all_sub_strings(original_string: str) -> list:

    sub_string = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    
    return list(sub_string)

def filter_sub_strings(sub_strings: list, k: int) -> list:
    
    sub_strings_filtered = [item for item in sub_strings if len(set(item)) == k]
    
    return sub_strings_filtered

###

sub_strings = get_all_sub_strings(string)

sub_strings = filter_sub_strings(sub_strings, k)

sub_strings.sort(key = len, reverse = True)
    
print(sub_strings[0])
