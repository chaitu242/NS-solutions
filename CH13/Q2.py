# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 06:58:05 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
x=np.linspace(0,1,101)
y = 1 + x + x * np.random.random(len(x))
A=np.vstack([x,np.ones(len(x))]).T
y=y[:,np.newaxis]
beta=np.dot(np.dot(np.linalg.inv(np.dot(A.T,A)),A.T),y)
print(beta)
plt.figure(figsize = (10,8))
plt.plot(x, y, 'g.')
plt.plot(x, beta[0]*x + beta[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()