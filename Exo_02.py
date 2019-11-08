# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:34:40 2019

@author: Nicolas Chataigneau
"""

print ("Saisir un entier strictement positif et superieur a 1 : ")

entier = int(input())
tab=[]
for i in range(2, entier+1):
    if entier % i == 0:
        tab.append(i)
        
print (tab)
