# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:58:20 2023

@author: Chaitanya Raju. Ch
"""
import numpy as np
def my_nuke_alarm(s1,s2,s3):
    lst=[s1,s2,s3]
    lst.sort()
    print(lst)
    print(np.abs(lst[2]-lst[0]))
    
    if np.abs(lst[2]-lst[0]) > 10:
        return("alarm")
    else:
        return("normal")
    