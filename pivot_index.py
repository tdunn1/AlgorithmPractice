# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:26:27 2023

@author: Tim
"""

#Find pivot index of array
def pivot_index(nums:list):
    S = sum(nums)
    left_sum = 0
    for i,x in enumerate(nums):
        if left_sum == S - left_sum - nums[i]:
            return i
        left_sum += x
    return -1

