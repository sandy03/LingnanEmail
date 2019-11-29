# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:36:20 2019

@author: Sandy Lin
"""
target=['a','b','c']
for i in range(4):
    try:
        print(target[i].upper())
    except IndexError:
        break