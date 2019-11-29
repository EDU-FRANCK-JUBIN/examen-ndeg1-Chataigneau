# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:51:37 2019

@author: Nicolas Chataigneau
"""

import easygui as ez

prenom = ""
nom = ""
telephone = ""
email = ""
nbPizza = 0

ez.multenterbox("Entrez les informations vous concernant : ","Informations du client",["Prenom","Nom","Telephone","Email"],[prenom,nom,telephone,email])
nbPizza = ez.integerbox("Combien voulez vous de pizza ?","Nombre de pizza", 1, 1, 10)


print(nbPizza)