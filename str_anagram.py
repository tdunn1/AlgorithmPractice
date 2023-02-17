# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:04:55 2023

@author: Tim
"""

from collections import Counter

#Returns start indices of where word is an anagram of s.
def is_anagram(chunk:str, word:str):
    return Counter(chunk) == Counter(word)

def anagram_indices(s:str, word:str):
    results = []
    for i in range(len(s) - len(word) + 1):
        chunk = s[i:i+len(word)]
        if is_anagram(chunk, word):
            results.append(i)
    
    return results
