# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:25:49 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n 
x = np.array([1, 1, 1])
a=[[2,1,2],[1,3,2],[2,4,1]]
for i in range(8):
    x = np.dot(a, x)
    lambda_1, x = normalize(x)
    print("Eigenvalue:", lambda_1)
    print("Eigenvector:", x)