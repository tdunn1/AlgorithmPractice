# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:36:42 2023

@author: Tim
"""

def bubble_swap(s:str, i:int, j:int):
    string = list(s)
    
    while i>0:
        string = string[1:] + string[:1]
        i -= 1
        
    #move first two characters reversed at end of string    
    string = string[:1] + string[2:] + string[1:2]
    string = string[1:] + string[:1]
    
    #to original positions
    while len(string) > j + 1:
        string = string[1:] + string[:1]
        j += 1
        
    return ''.join(string)

