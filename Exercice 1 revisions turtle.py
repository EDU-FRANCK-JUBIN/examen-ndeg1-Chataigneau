# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:23:26 2019

@author: Nicolas Chataigneau
"""

import turtle as tu

print("Choose hight of the tree as a number : ")
hight = 12
treeComponent = "^"
lineToDraw = treeComponent

screen = tu.Screen()
screen.setup(800,600)

tree = tu.Turtle()
tree.speed(5)
tree.width(3)
tree.color("green")
tree.write(lineToDraw)

i= 1

while i < hight:
    tree.goto(0,-i-1)
    lineToDraw = treeComponent + treeComponent
    tree.write(lineToDraw)
    i = i + 1


tu.exitonclick()