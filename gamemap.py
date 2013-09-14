# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import character
import mapobject

def testmap():
    objects = [character.normalplayer(0, [0,0,0],[0,0,0],[0,10])
               ,character.normalenemy(0,[5,0,5],[0,0,0],[1,10])
               ,character.normalenemy(1,[10,0,10],[0,0,0],[1,10])
               ,mapobject.wall((0,0,0),(100,0,0),100)
               ,mapobject.floor((0,0,0),100,100)]
    

    return objects
