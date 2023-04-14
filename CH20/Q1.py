# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:27:42 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
import matplotlib.pyplot as plt
h=0.1
x=np.arange(0,2*np.pi,h) 
y=np.cos(x) 
forwarddiff=np.diff(y)/h 
xdiff = x[:-1:] 
exactsolution = -np.sin(xdiff) 
plt.figure(figsize = (12, 8))
plt.plot(xdiff, forwarddiff, '--', \
         label='Finite difference approximation')
plt.plot(xdiff, exactsolution, \
         label='Exact solution')
plt.legend()
plt.show()
max_error=max(abs(exactsolution-forwarddiff))
print(max_error)