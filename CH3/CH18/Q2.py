# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:36:38 2023

@author: Chaitanya Raju. Ch
"""

import math
import numpy as np
x=2
e_to_taylor=0
for i in range(7):
    e_to_taylor += x**i/math.factorial(i)
    print(f"Using {i}- term = {e_to_taylor}")
    print ("Actual value using Taylor Series= ",e_to_taylor)
    print ("\n")
    exp_py=math.exp(x)
    print ("Actual value Using math=",exp_py)
    print ("\n")
    exp_np=np.exp(2)
    for i in range(7):
        exp_np=np.exp(2)
        print(f"Using {i}- term = {exp_np}")
        print ("Actual Value Using numpy=",exp_np)
        print ("Truncation error is = ",abs(e_to_taylor-np.exp(2)))