# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:15:37 2023

@author: Chaitanya Raju. Ch
"""

class student():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def info(self):
        print("Name of student:",self.name)
    def report(self,score):
        print("Score",str(score))
s1=student(name="gill",age=23,gender="M")
s1.info()
s1.report(66)