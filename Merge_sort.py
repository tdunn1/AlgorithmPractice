# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:28:07 2023

@author: Tim
"""

def last_idx(array:list) -> int:
    return len(array)-1

def merge(array:list, p:int, q:int, r:int) -> list:
    n1 = q-p+1
    n2 = r-q
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = array[p+i]
    for j in range(n2):
        R[j] = array[q+j+1]
    L[-1] = float('inf')
    R[-1] = float('inf')
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
            
    return array

def merge_sort(array:list, p, r) -> list:
    
    if p<r:
        q = (p+r)//2
        merge_sort(array,p,q)
        merge_sort(array,q+1,r)
        merge(array,p,q,r)
        
test = [2,4,5,7,1,2,3,6]
merge_sort(test,0,last_idx(test))
print(test)

