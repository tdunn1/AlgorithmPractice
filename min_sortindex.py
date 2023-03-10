# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:33:55 2023

@author: Tim
"""

#Find minimum index range to sort array.
def min_sortindex(nums:list):
    
    left,right = None,None
    n = len(nums)
    max_seen, min_seen = -float('inf'), float('inf')
    
    for i in range(n):
        max_seen = max(max_seen, nums[i])
        if nums[i] < max_seen:
            right = i
            
    for i in range(n-1,-1,-1):
        min_seen = min(min_seen,nums[i])
        if nums[i] > min_seen:
            left = i
            
    return left, right
