# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 02:36:01 2023

@author: Chaitanya Raju. Ch
"""

def my_pascal_row(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        row = [1]
        last_row = my_pascal_row(n-1)
        for i in range(1,len(last_row)):
            row.append(last_row[i-1] + last_row[i])
            row += [1]
        return row