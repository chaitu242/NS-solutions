# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 02:36:36 2023

@author: Chaitanya Raju. Ch
"""

def make_change(amt, lis):
    deno=[100,50,20,10,5,1, .5, .25, .1, .05, .01]
    i=0
    if amt > 0.009:
        while deno[i] > amt:
            i+=1
        amt -= deno[i]
        lis.append(deno[i])
    else:
        return lis
    return make_change(amt,lis)