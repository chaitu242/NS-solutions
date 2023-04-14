# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:26:29 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
newton_raphson = 1.4 - (f(1.4))/(f_prime(1.4))
print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))
def my_newton(f,df,x0,tol):
    if abs(f(x0))<tol:
        return x0
    else:
        return my_newton(f, df, x0-f(x0)/df(x0), tol)
estimate = my_newton(f, f_prime, 1.5, 1e-6)
print("estimate =", estimate)
print("sqrt(2) =", np.sqrt(2))
