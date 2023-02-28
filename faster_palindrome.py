# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:41:28 2023

@author: Tim
"""

def is_palindrome(s:str) -> bool:
    return s == s[::-1]

def palindrome_indices(words:list) -> list:
    results = []
    word_dict = {}
    
    for i,word in enumerate(words):
        word_dict[word] = i
        
    for i,word in enumerate(words):
        for i_char in range(len(word)):
            prefix,suffix = word[:i_char], word[i_char:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]
            
            if is_palindrome(prefix) and reversed_suffix in word_dict:
                if i != word_dict[reversed_suffix]:
                    results.append((word_dict[reversed_suffix], i))
                    
            if is_palindrome(suffix) and reversed_prefix in word_dict:
                if i != word_dict[reversed_prefix]:
                    results.append((i, word_dict[reversed_prefix]))
                
            
                
    return results
    
