# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:14:24 2023

@author: Chaitanya Raju. Ch
"""

class people():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greets(self):
        print("hello",self.name)
p1=people(name="gill", age=23)
p1.greets()
print(p1.name)