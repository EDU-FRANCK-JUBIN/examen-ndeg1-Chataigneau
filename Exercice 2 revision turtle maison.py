# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:03:30 2019

@author: Nicolas Chataigneau
"""

import turtle as tu
import math

screen = tu.Screen()
screen.setup(800,600)

house = tu.Turtle()

house.fd(80)
house.lt(90)
house.fd(80)

house.lt(30)
house.color("green")
house.fd(80)
house.lt(120)
house.fd(80)

house.color("black")
house.lt(120)
house.fd(80)
house.lt(180)
house.fd(80)

house.lt(90)
house.fd(80)
house.lt(90)
house.fd(20)
house.lt(90)

house.color("red")
house.fd(40)
house.rt(90)
house.fd(40)
house.rt(90)
house.fd(40)

tu.exitonclick()