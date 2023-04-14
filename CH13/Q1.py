# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:06:12 2023

@author: Chaitanya Raju. Ch
"""
import numpy as np
import matplotlib.pyplot as plt
r=3
z=np.linspace(0,20*np.pi,1000)
y=r*(1-np.cos(z))
x=r*(z-np.sin(z))
plt.figure(figsize=(8,6))
plt.plot(x,y)
plt.show()