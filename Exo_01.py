# -*- coding: utf-8 -*-

import math

print ("Entrez une valeur pour le rayon : ")
rayon = int(input())

print ("Entrer une valeur pour la hauteur :")
hauteur = int(input())

volume = math.pi * rayon*rayon * hauteur / 3

print(volume)
