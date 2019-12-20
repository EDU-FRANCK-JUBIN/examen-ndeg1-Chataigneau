# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:25:40 2019

@author: Nicolas Chataigneau
"""

from easygui import * 


gui.msgbox("Bienvenue dans notre restaurant, nous proposons des plats venus d'Asie ou d'Europe de l'ouest.")

msg ="Que choisissez vous ?"
title = "Choix du plat"
choices = ["Asie", "Europe de l'ouest"]
choice = gui.choicebox(msg, title, choices)