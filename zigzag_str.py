# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:58:37 2023

@author: Tim
"""

import pdb
def spaces_num(k:int, row:int, desc:bool) -> int:
    row_ind = row + 1
    max_spaces = 2*(k-1) - 1
    if desc:
        spaces = max_spaces - 2*(row_ind)
    else:
        spaces = max_spaces - 2*(k - row)
    return spaces

def is_desc(k, i:int) -> bool:
    index = i + 1
    return index % (2*k) < k
