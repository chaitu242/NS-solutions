# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:15:09 2023

@author: Chaitanya Raju. Ch
"""

class student():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def info(self):
        print("hello this is",self.name,"age",self.age,"gender",self.gender)
s1=student(name="samson", age=20, gender="M")
s1.info()