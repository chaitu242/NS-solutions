# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:35:28 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
def my_double_exp(x, n):
    for i, j in zip(x, n):
        exp = 0
        var = i
        for order in range(j):
            exp = exp + (var)**(2*order)/np.math.factorial(order)
    print(f"Using first {j} terms for x = {i}, the approximation is {exp}")
    print(f"True value of e^2^2 is: {np.exp(2**2)}")
