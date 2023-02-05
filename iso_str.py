# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:36:01 2023

@author: Tim
"""

def string_isomorph(str1, str2):
    dict1 = {}
    dict2 = {}
    
    for a,b in zip(str1,str2):
        if a not in dict1 and b not in dict2:
            dict1[a] = b
            dict2[b] = a
        
        # if character not mapped or incorrectly mapped
        elif dict1.get(a) != b or dict2.get(b) != a:
            return False
        
    return True

s = 'egg'
t = 'add'

print(string_isomorph(s,t))