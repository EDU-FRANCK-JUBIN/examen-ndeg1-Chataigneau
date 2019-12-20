# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:01:10 2019

@author: Nicolas Chataigneau
"""
import random
import turtle as tu

screen = tu.Screen()
screen.setup(800, 600)


isEnded = False

Michelangelo = tu.Turtle()
Leonardo = tu.Turtle()
Raphael = tu.Turtle()
Splinter = tu.Turtle()

Michelangelo.shape("turtle")
Michelangelo.color("Orange")
Michelangelo.setposition(-100, 80)

Leonardo.shape("turtle")
Leonardo.color("Deep Sky Blue")
Leonardo.setposition(-100, 40)

Raphael.shape("turtle")
Raphael.color("Red")
Raphael.setposition(-100, 0)

Splinter.shape("turtle")
Splinter.color("Dark Slate Gray")
Splinter.setposition(-100, -40)

print("Joueur 1 : D'après vous quel sera le classement?")

print("Pour Michelangelo ?")
MichelangeloClass1 = input()

print("Pour Leonardo ?")
LeonardoClass1 = input()

print("Pour Raphael ?")
RaphaelClass1 = input()

print("Pour Splinter ?")
SplinterClass1 = input()

print("Joueur 2 : D'après vous quel sera le classement?")

print("Pour Michelangelo ?")
MichelangeloClass2 = input()

print("Pour Leonardo ?")
LeonardoClass2 = input()

print("Pour Raphael ?")
RaphaelClass2 = input()

print("Pour Splinter ?")
SplinterClass2 = input()

while not isEnded:
    # print("Saisir une distance à parcourir entre 1 et 5 :")
    goForward = random.randint(1, 5)
    Michelangelo.forward(goForward)

    goForward = random.randint(1, 5)
    Leonardo.forward(goForward)

    goForward = random.randint(1, 5)
    Raphael.forward(goForward)

    goForward = random.randint(1, 5)
    Splinter.forward(goForward)

    if Michelangelo.position == (500, 80) or Leonardo.position == (500, 40) or Raphael.position == (
            500, 0) or Splinter.position == (500, -40):
        isEnded = True

tu.exitonclick()
