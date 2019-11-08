# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:22:16 2019

@author: Nicolas Chataigneau
"""

def minMaxMoy(listEntier):
    
    min=listEntier[0]
    max=0
    moy=0
    nbEntier = 0
    
    for value in listEntier:
        if min>value:
            min = value
        if max<value:
            max = value
            
        nbEntier = nbEntier+1
        
    for i in range(1, nbEntier):
        moy = listEntier[i] + moy
    
    moy = moy / nbEntier
    
    return (min,max,moy)
        
    
myListEntier=[35,20,52]
print(minMaxMoy(myListEntier))