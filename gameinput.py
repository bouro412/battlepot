from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def keyb(key, x, y,ws,ad):

    if key == '\033':
        print "exit..."
        exit()
    if key == 'w':
        ws = 1
    if key == 's':
        ws = -1
    if key == "a":
        ad = 1
    if key == "d":
        ad = -1
    return (ws, ad)

def keyup(key,x,y,ws,ad):
 
    if key == "w":
        ws = 0
    if key == "s":
        ws = 0
    if key == "a":
        ad = 0
    if key == "d":
        ad = 0
    
    return (ws, ad)

