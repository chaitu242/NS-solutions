# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:29:42 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,2*np.pi,0.01) 
omega=100
epsilon=0.01
y=np.cos(x) 
y_noise=y+epsilon*np.sin(omega*x)
plt.figure(figsize=(12,8))
plt.plot(x, y_noise,'r-', \
         label='cos(x)+noise')
plt.plot(x, y,'b-', \
         label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()