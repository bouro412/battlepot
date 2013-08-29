# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import character
import mapobject

def testmap():
    p1 = character.normalplayer(0, [0,0,0],[0,0,0],[0,10])
    e1 = character.normalenemy(0,[5,0,5],[0,0,0],[1,10])
    e2 = character.normalenemy(1,[10,0,10],[0,0,0],[1,10])
    floor = mapobject.floor((0,0,0),100,100)
    objects = [p1,e1,e2,floor]
    return objects
