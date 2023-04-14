# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:19:54 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
def my_is_orthogonal(v1, v2, tol):
    dot_product = np.dot(v1, v2)
    norm_product = np.linalg.norm(v1) * np.linalg.norm(v2)
    cos_theta = dot_product / norm_product
    theta = np.arccos(cos_theta)
    return 1 if abs(np.pi/2 - theta) < tol else 0
a = np.array([[1], [0.001]])
b = np.array([[0.001], [1]])
my_is_orthogonal(a,b, 0.01)
