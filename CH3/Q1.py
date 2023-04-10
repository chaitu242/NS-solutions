# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 07:39:37 2023

@author: Chaitanya Raju. Ch
"""

import numpy as np
def my_checker_board(n):
    x=np.zeros((n,n))
    for i in range  (n):
        for j in range(n):
          if i%2==0:
              if j%2==0:
                  x[i,j]=1
              else:
                  x[i,j]=0
          else:
              if j%2==0:
                  x[i,j]=0
              else:
                  x[i,j]=1
        
