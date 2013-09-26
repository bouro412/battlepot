# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import character
import mapobject

def testmap():
    objects = [character.normalplayer(0, [100,0,100],[0,0,0],[0,10])
               ,character.normalenemy(0,[50,0,50],[0,0,0],[1,10,3])
               ,character.normalenemy(1,[150,0,150],[0,0,0],[2,10,2])
               ,mapobject.wall((0,0,0),(200,0,0),100)
               ,mapobject.floor((0,0,0),200,200)]
    

    return objects
