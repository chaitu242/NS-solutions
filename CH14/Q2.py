# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:19:38 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
s=np.array([[1,1,2],[2,4,5],[7,8,10]])
f=np.array([1,2,3])
print(np.dot(s,f))
x=np.linalg.solve(s,f)
print(x)