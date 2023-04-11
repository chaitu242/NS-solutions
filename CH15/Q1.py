# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:24:34 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
from numpy.linalg import qr
a = np.array([[0, 2], 
              [2, 3]])
q, r = qr(a)
print('Q:', q)
print('R:', r)
b = np.dot(q, r)
print('QR:', b)
a = np.array([[0, 2], 
              [2, 3]])
p = [1, 5, 10, 20]
for i in range(20):
    q, r = qr(a)
    a = np.dot(r, q)
    if i+1 in p:
        print(f'Iteration {i+1}:')
        print(a)