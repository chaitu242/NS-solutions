# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:21:57 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
A = np.vstack([x, np.ones(len(x))]).T
y = y[:, np.newaxis]
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
print(alpha)
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
pinv = np.linalg.pinv(A)
alpha = pinv.dot(y)
print(alpha)
alpha = np.linalg.lstsq(A, y, rcond=None)[0]
print(alpha)
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
def func(x, a, b):
    y = a*x + b
    return y
alpha = optimize.curve_fit(func, xdata = x, ydata = y)[0]
print(alpha)