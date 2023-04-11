# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:23:09 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([0,0.8,0.9,0.1,-0.6,-0.8,-1,-0.9,-0.4,2])
A=np.vstack([x,np.ones(len(x))]).T
plt.figure(figsize=(24,10))
i=2
plt.subplot(2,3,i)
plt.plot(x,y,"o")
plt.plot(x,y_est[0]*x**2+y_est[1]*x+0,"r",label="multivariant regression")
plt.title(f"Polynomial of order{i}Least square regression formula")
plt.legend()
plt.tight_layout()
plt.show()