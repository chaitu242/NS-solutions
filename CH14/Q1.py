# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:18:38 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
from np.linalg import norm
from numpy import arccos, dot
v=np.array([[10,9,3]])
w=np.array([[2,5,12]])
theta =arccos(dot(v, w.T)/(norm(v)*norm(w)))
print(theta)
v=np.array([[0,2,0]])
w=np.array([[3,0,0]])
print(np.cross(v,w))
P=np.array([[1,7],[2,3],[5,0]])
Q=np.array([[2,6,3,1],[1,2,3,4]])
print(P)
print(Q)
print(np.dot(P,Q))
np.dot(Q,P)