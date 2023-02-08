# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:35:21 2023

@author: Tim
"""

#Find largest contiguous subarray sum allowing for wrap around.
def array_sub_sum(array):
    wrap_around_sum = sum(array) - min_sub(array)
    
    return max(wrap_around_sum, max_sub(array))


def max_sub(array):
    max_so_far, max_to_here = 0,0
    
    for x in array:
        max_to_here = max(x, max_to_here + x)
        max_so_far = max(max_to_here, max_so_far)
        
    return max_so_far

def min_sub(array):
    min_so_far, min_to_here = 0,0
    
    for x in array:
        min_to_here = min(x, min_to_here + x)
        min_so_far = min(min_to_here, min_so_far)
        
    return min_so_far
