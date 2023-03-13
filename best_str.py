# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:51:34 2023

@author: Tim
"""

def get_best_str(s:str, k):
    string = list(s)
   
    
    if k == 1:
        best = string
        for i in range(1,len(string)):
            if string[i:] + string[:i] < best:
                best = string[i:] + string[:i]
        return ''.join(best)
    
    else:
        return ''.join(sorted(string))
    


        
