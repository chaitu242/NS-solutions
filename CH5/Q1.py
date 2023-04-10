# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 01:23:05 2023

@author: Chaitanya Raju. Ch
"""
def my_saving_plan(p0,i,goal):
    p=1
    count=0
    while p<goal: 
     p=(1+i)*p0
     p0=p
     count+=1
    return count
     