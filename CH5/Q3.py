# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 01:57:05 2023

@author: Chaitanya Raju. Ch
"""
import numpy as np

def my_n_fib_primes(n):
    fib = np.ones(n)
    lst=[]
    count=0
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    print(fib)
    for j in fib:
        for k in range(2,n):
            
           
           if j%k!=0:
                count+=1
        if count==n-1: 
         lst.append(j)
    return lst
                
        
        