# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:29:40 2023

@author: Tim
"""

#Returns product of all other elements.
def array_prod(nums:list):
    prefix_prod = []
    
    for num in nums:
        if prefix_prod:
            prefix_prod.append(prefix_prod[-1] * num)
        else:
            prefix_prod.append(num)
    
    suffix_prod = []
    
    for num in reversed(nums):
        if suffix_prod:
            suffix_prod.append(suffix_prod[-1] * num)
        else:
            suffix_prod.append(num)
            
    suffix_prod = list(reversed(suffix_prod))
    
    result = []
    
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_prod[i+1])
        elif i == len(nums) - 1:
            result.append(prefix_prod[i-1])
        else:
            result.append(prefix_prod[i-1]*suffix_prod[i+1])
            
    return result
