# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:37:18 2021

@author: Gebruiker
"""

"""
Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

import pandas as pd

array = [(30, 75), (0, 50), (60, 150), (15,50), (60, 150), (60, 150)]


def find_minimal_number_rooms(array: list) -> int:
    
    for i in array:
        
        #check for tuples
        if not(isinstance(i, tuple)):
            raise ValueError('Please only input tuples')
        
        #check for valid tuples
        elif len(i) != 2:
            raise ValueError('Please input a list of tuples of len(2)')
        
        #check that begining is lower than end
        elif i[0] >= i[1]:
            raise ValueError('Make sure that tuples begin and end properly')
    
    starts = []
    ends = []
    
    for i in array:
        starts.append(i[0])
        ends.append(i[1])
        
    start = min(starts)
    end = max(ends)
    
    df_timeline = pd.DataFrame({'Timeline': list(range(start,end+1))}).set_index('Timeline')
    
    iterator = 1
    
    for i in array:
        iterator += 1
        
        df = pd.DataFrame({f'Course{iterator}': range(i[0],i[1]+1)
                           ,f'CounterCourse{iterator}': [1] * (i[1]-i[0]+1)}).set_index(f'Course{iterator}')
        
        df_timeline = df_timeline.join(df)
    
    df_timeline['Total'] = df_timeline.sum(axis=1, numeric_only= True)
    
    answer = int(max(df_timeline['Total']))
    
    return answer

print(find_minimal_number_rooms(array))



    