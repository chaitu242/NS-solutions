# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:25:43 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
def my_bijection(f,a,b,tol):
    if np.sign(f(a))==np.sign(f(b)):
        return "invalid"
    m=(a+b)/2
    if np.abs(f(m))<tol:
        return m
    elif np.sign(f(a))==np.sign(f(m)):
        return my_bijection(f, m, b, tol)
    elif np.sign(f(b))==np.sign(f(m)):
        return my_bijection(f, a, m, tol)
def f(x):
    return x**3 - 3*x + 1
root = my_bijection(f, 0, 1)
print(root)