# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:27:02 2021

@author: Gebruiker
"""

"""
Staircase with N number of steps.
You can take an array of number of steps at the same time (X)
Write a function num_ways(N,X) that returns the number of ways you can reach the final step.
"""

def num_ways(step_number: int, allowed_steps: list) -> int:
    curr_step = step_number
    for a in allowed_steps:
        if curr_step