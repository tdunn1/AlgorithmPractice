# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:26:27 2023

@author: Tim
"""
# import pdb
def pivot_index(nums):
    S = sum(nums)
    left_sum = 0
    for i,x in enumerate(nums):
        if left_sum == S - left_sum - nums[i]:
            return i
        left_sum += x
    return -1
# pdb.set_trace()
nums = [1,7,3,6,5,6]
print(pivot_index(nums))