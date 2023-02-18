# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:47:09 2023

@author: Tim
"""

from collections import defaultdict

#Faster anagram checker
def del_zero_key(dft_dict, key):
    if dft_dict[key] == 0:
        del dft_dict[key]
        
def anagram_ind(s:str, word:str):
    
    results = []
    
    char_occ = defaultdict(int)
    
    for char in word:
        char_occ[char] += 1
        
    for char in s[:len(word)]:
        char_occ[char] -= 1
        del_zero_key(char_occ, char)
        
    if not char_occ:
        results.append(0)
        
    for i in range(len(word),len(s)):
        start_char, end_char = s[i-len(word)],s[i]
        char_occ[start_char] += 1
        del_zero_key(char_occ, start_char)
        char_occ[end_char] -= 1
        del_zero_key(char_occ, end_char)
        
        if not char_occ:
            index = i - len(word) + 1
            results.append(index)
        
    return results

s = 'abxaba'
w = 'ab'

print(anagram_ind(s, w))