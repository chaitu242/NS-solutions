# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:38:35 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
def my_inside_triangle(x,y):
    if x+y==1:
        return("border")
    elif x>0 and x<1:
        if y>0 and y<1:
            return("inside")
        else:
            return("outside")
    else:
        return("outside")