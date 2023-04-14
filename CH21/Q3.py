# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:37:34 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
a=0
b=np.pi
n=11
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)
I_simp=(h/3)*(f[0]+2*sum(f[:n-2:2])+4*sum(f[1:n-1:2])+f[n-1])
err_simp=2-I_simp
print(I_simp)
print(err_simp)