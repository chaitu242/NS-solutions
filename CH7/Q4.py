# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:16:04 2023

@author: Chaitanya Raju. Ch
"""

import matplotlib.pyplot as plt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def plot_point(self):
        plt.scatter(self.x, self.y)
        plt.show()
p = Point(1, 2)
p.plot_point()