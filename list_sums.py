# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:09:01 2023

@author: Tim
"""
#Returns running sum of an array.
def array_sum(nums:list):
    l = len(nums)
    s = [0]*l
    s[0] = nums[0]
    for i in range(1, l):
        s[i] = s[i-1] + nums[i]
    return s
