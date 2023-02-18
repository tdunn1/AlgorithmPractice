# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:32:55 2023

@author: Tim
"""

def is_palindrome(word:str):
    if len(word)%2 == 0:
        return word[:len(word)//2] == word[-1:len(word)//2-1: -1]
    else:
        return word[:len(word)//2] == word[-1:len(word)//2: -1]

def palindromes(words:list):
    
    results = []
    
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            merge_word_1 = ''.join([words[i],words[j]])
            merge_word_2 = ''.join([words[j],words[i]])
            if is_palindrome(merge_word_1):
                results.append((i,j))
            if is_palindrome(merge_word_2):
                results.append((j,i))
                
    return results

