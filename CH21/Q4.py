# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:38:03 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
from scipy.integrate import trapz
a= 0
b=np.pi
n=11
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)
I_trapz=trapz(f,x)
I_trap=(h/2)*(f[0]+2*sum(f[1:n-1])+f[n-1])
print(I_trapz)
print(I_trap)