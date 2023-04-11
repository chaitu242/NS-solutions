# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 02:42:36 2023

@author: Chaitanya Raju. Ch
"""

def my_dec_2_bin(d):
    b=[]
    if d==0:
        b.append(0)
    while d>= 1:
         b.append(d%2)
         d= d//2
         b.reverse()
         return b;