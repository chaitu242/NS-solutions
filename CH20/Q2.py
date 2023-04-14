# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:28:41 2023

@author: Chaitanya Raju. Ch
"""
import numpy as np
import matplotlib.pyplot as plt
h=1
iterations = 20 
step_size=[] 
max_error=[] 
for i in range(iterations):
    h /= 2 
    step_size.append(h) 
    x=np.arange(0,2*np.pi,h) 
    y=np.cos(x) 
    forward_diff=np.diff(y)/h 
    x_diff = x[:-1] 
    exact_solution = -np.sin(x_diff) 
    max_error.append(\
            max(abs(exact_solution - forward_diff)))
plt.figure(figsize = (12, 8))
plt.loglog(step_size, max_error, 'v')
plt.show()