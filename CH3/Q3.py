# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:23:35 2023

@author: Chaitanya Raju. Ch
"""
import numpy as np
def my_within_tolerance(A,a,tol):
    x=np.array([])
    for i in A:
        if np.abs(i-a) < tol:
            x=np.append(x,i)
    return x
            