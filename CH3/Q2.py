# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:04:15 2023

@author: Chaitanya Raju. Ch
"""
import numpy as np
def mysplitmatrix(m):
    y=m.shape
    if y[1]%2==0:
        m1=m[:,:(y[1]//2)]
        m2=m[:,(y[1]//2):]
    else:
        m1=m[:,:((y[1]-1)//2+1)]
        m2=m[:,((y[1]-1)//2+1):]
    return m1,m2