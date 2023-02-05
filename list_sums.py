# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:09:01 2023

@author: Tim
"""

def array_sum(nums):
    l = len(nums)
    s = [0]*l
    s[0] = nums[0]
    for i in range(1, l):
        s[i] = s[i-1] + nums[i]
    return s
nums = [1,2,7,0,4]
print(nums, '\n',array_sum(nums))