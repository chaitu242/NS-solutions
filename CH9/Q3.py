# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 02:44:41 2023

@author: Chaitanya Raju. Ch
"""

def my_bin_2_dec(b):
    d=0
    for digit in b:
        d=d*2 +int(digit)
        return d;