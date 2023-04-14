# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:36:35 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
a=0
b=np.pi
n=11
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)
I_r=h* sum(f[:n-1])
err_r=2-I_r
I_R=h*sum(f[1::])
err_R=2-I_R
I_mid=h*sum(np.sin((x[:n-1]+x[1:])/2))
err_mid=2-I_mid
print(I_r)
print(err_r)
print(I_R)
print(err_R)
print(I_mid)
print(err_mid)