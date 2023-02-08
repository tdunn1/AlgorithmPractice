# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:07:18 2023

@author: Tim
"""

#Determines if str s is a subsequence of str t.
def sub_seq(s:str,t:str) -> bool:
    
    if len(s) > len(t): 
        return False
    
    if len(s) == 0: 
        return True
    
    i,j = 0,0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
        
    return True if i == len(s) else False
