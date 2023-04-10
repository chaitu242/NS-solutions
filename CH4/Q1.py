# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:27:54 2023

@author: Chaitanya Raju. Ch
"""
import numpy as np
def my_make_size10(x):
    if x.size>=10:
        return(x[:11])
    else:
        x=np.append(x,np.zeros(10-x.size))
        return(x)
        
