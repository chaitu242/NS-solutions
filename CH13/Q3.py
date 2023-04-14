# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:00:39 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-11, 11,200)
plt.plot(x,x**6,"bo")
plt.plot()
#4
x = np.linspace(-5,5,20)
plt.plot(x, x**2, 'ko')
plt.plot(x, x**3, 'r*')
plt.show()