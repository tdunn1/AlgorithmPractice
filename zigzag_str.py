# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:58:37 2023

@author: Tim
"""

def spaces_num(k:int, row:int, desc:bool) -> int:
    row_ind = row + 1
    if desc:
        spaces = 2*(k-row_ind) - 1
    else:
        max_spaces = 2*(k-1) - 1
        spaces = max_spaces - 2*(k - row_ind)
    return spaces

def is_desc(k, i:int) -> bool:
    index = i 
    return index % (2*(k) - 2) < k-1

def zig_zag(sentence:str, k):
    sent_len = len(sentence)
        
    for row in range(k):
        i = row
        line = [' ' for _ in range(sent_len)]
        
        while i < sent_len:
            line[i] = sentence[i]
            desc = is_desc(k, i)
            spaces = spaces_num(k,row, desc)
            i += spaces + 1
            
        print(''.join(line))
    
