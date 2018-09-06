#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:42:29 2018

@author: stephaneblondellarougery
"""

def count_tables(db):
    # Le dernier -1 correspond au worksheet 'SQL' à ne pas prendre en compte
    try:
        count = int(str(db)[len(str(db))-3:len(str(db))-1])-1 
        return count
    except:
        return int(str(db)[len(str(db))-2])-1 

def is_up(ch):
    try:
        int(ch)
        return True
    except:
        return ch.lower() != ch

def is_jar(word):
    r = 0 
    for ch in word:
        if ch == "_":
            r += 1 
    return r == 0
    
def is_py(word):
    r = 0 
    for ch in word:
        if ch != ch.lower():
            r += 1
    return r == 0
    
    
def jar_to_py(word):
    # Transforme les mots avec une convention Java en convention Python
    if is_jar(word):
        new_word = word[0].lower()
        for ch in word[1:]:
            if is_up(ch):
                new_word += "_"
                new_word += ch.lower()
            else:
                new_word += ch   
        return new_word
                
    
def py_to_jar(word):
    # Transforme les mots avec une convention Python en convention Java
    if is_py(word):
        new_word = word[0].upper()
        UP = 0
        for ch in word[1:]:
            if ch == "_":
                UP = 1
            elif UP == 1:
                new_word += ch.upper()
                UP = 0  
            else:
                new_word += ch 
        return new_word
    
def parse_py(word):
    L = []
    if is_py(word):
        L = word.split("_")
    return L

def parse_jar(word):
    L = []
    if is_jar(word):
        word = jar_to_py(word)
        L = word.split("_")
    return L

def make_py(L):
    w = ""
    if len(L) == 1:
        w = L[0]
    elif len(L) > 1:
        w = L[0]
        for word in L[1:]:
            w+="_"
            w+=word.lower()
    return w

def make_jar(L):
    return py_to_jar(make_py(L))
        

def plural_jar(word):
    if is_jar(word):
        L = parse_jar(word)
        L[0] = L[0] + "s"
        return make_jar(L)
    
def plural_py(word):
    if is_py(word):
        L = parse_py(word)
        L[0] = L[0] + "s"
        return make_py(L)
    
def plural(word):
    if is_py(word):
        return plural_py(word)
    elif is_jar(word):
        return plural_jar(word)