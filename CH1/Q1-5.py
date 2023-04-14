# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:08:42 2023

@author: Chaitanya Raju. Ch
"""

#1
h=12
b=10
area=0.5*b*h
print(area)
#2
import math
x1=3
y1=4
x2=5
y2=9
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)
#3
def fac(n):
    if n==1 or n==0:
        return 1
    else: 
        return n*fac(n-1)
print(fac(6))
#4
def leap(year):
    for i in range(1500,2011):
        if i%4==0 and (i%100!=0 or i%400==0):
            output="it is a leap year"
            return output
        else:
            output="not a leap year"
            return output