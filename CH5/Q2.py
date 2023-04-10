# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 01:32:31 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
def my_trig_odd_even(M):
    x=M.shape
    q=np.empty((x))
    for i in range (x[0]):
        for j in range(x[1]):
            if M[i,j]%2!=0:
                q[i,j]==np.sin(np.pi/M[i,j])
            else:
                q[i,j]==np.cos(np.pi/M[i,j])
    return q