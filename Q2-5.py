# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:12:24 2023

@author: Chaitanya Raju. Ch
"""

s1='HELLO'
s2='hello'
print(s1==s2)  
print(s1.lower()==s2)  
print(s1==s2.upper()) 
#3
l1=[1,8,9,15]
l1.insert(1,2)
l1.append(4)
print(l1)
#4
s1="python is great"
print(list(s1))
#5
set_a=set([2,3,2])
set_b=set([1,2,3])
union=set_a.union(set_b)
intersection=set_a.intersection(set_b)
difference=set_a.difference(set_b)
print(union)
print(intersection)
print(difference)