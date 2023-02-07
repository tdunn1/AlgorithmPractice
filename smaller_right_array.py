# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:14:48 2023

@author: Tim
"""
import bisect
import pdb

#Find number of elements smaller and to the right of each element
def small_elements_r(array:list):
    result = []
    seen = []
    
    for num in reversed(array):
        i = bisect.bisect_left(seen,num)
        result.append(i)
        bisect.insort(seen,num)
        
    return list(reversed(result))

x = [3,4,9,6,1]
pdb.set_trace()
print(small_elements_r(x))
