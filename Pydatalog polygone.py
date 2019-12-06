"""
Created on Mon Dec  2 19:29:51 2019

@author: Nicolas Chataigneau
"""

from pyDatalog import pyDatalog
pyDatalog.clear()

pyDatalog.create_terms('ordre', 'triangle', 'triangleisocele', 'coteegaux', 'trianglerectangle','angledroit','triangleeqquilateraux','X','Y')

#triangle
triangle(X) <= ordre(X,Y) & Y==3
trianglerectangle(X) <= triangle(X) & angledroit(X)
triangleisocele(X) <= triangle(X) & coteegaux(X,Y) & Y==2
triangleequilateraux(X) <= triangle(X) & coteegaux(X,Y) & Y==3