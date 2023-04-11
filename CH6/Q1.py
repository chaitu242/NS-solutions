# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 02:34:13 2023

@author: Chaitanya Raju. Ch
"""

def my_spiral_ones(n):
    if ( n == 0 ):
        print(" invalid")
        
    if ( n == 1 ):
        return [1]
    tempA = my_spiral_ones(n-1)
    if ( n == 2 ):
        tempA = [ tempA ]
        sumBottom = 0
        sumTop = -1
    elif ( n == 3 ):
        sumBottom = -1
        sumTop = -1
    else :
            sumTop = sum ( tempA[0] )
            sumBottom = sum ( tempA[-1] )
            resultA = None
            if ( sumBottom == n-2 ) :
                resultA = tempA + [[0 for x in range (n-1) ]]