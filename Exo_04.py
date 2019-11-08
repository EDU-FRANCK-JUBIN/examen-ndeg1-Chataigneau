# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:45:36 2019

@author: Nicolas Chataigneau
"""

def valide(saisie):
    
    nbOK = 0
    
    for adn in saisie :
        if adn == "a" or adn == "t" or adn == "g" or adn == "c" :
            nbOK = nbOK+1
            
    if nbOK == 4 :
        return True
    else:
        return False
    
mySaisie = ["g","a","c","t"]
print (valide(mySaisie))

def saisie(saisieValide):
    
    chain = ""
    
    for caract in saisieValide:
        chain = chain + caract
    
    return chain

print (saisie(["g","a","c","t"]))

def proportion(mySaisie, saisieValide):
    
    nbOccurence = 0
    
    return nbOccurence