# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import character
import mapobject

def testmap():
    objects = [character.normalplayer(0, [20,0,50],[0,0,0],[0,10])
               ,character.normalenemy(0,[50,0,50],[0,0,0],[1,10,3])
               ,character.normalenemy(1,[150,0,150],[0,0,0],[2,10,2])
               #,mapobject.wall((0,0,0),(200,0,0),100)
               ,mapobject.floor((0,0,0),100,100)
               ,mapobject.floor((0,10,0),90,5)
               ,mapobject.floor((0,5,5),90,5)
               ,mapobject.floor((0,5,90),90,5)
               ,mapobject.floor((0,10,95),90,5)
               ,mapobject.floor((90,10,0),10,100)
               ,mapobject.wall((0,0,0),(0,0,100),100)
               ,mapobject.wall((0,0,0),(100,0,0),100)
               ,mapobject.wall((100,0,0),(100,0,100),100)
               ,mapobject.wall((0,0,100),(100,0,100),100)
               ,mapobject.wall((0,0,10),(90,0,10),5)
               ,mapobject.wall((0,5,5),(90,2,5),5)
               ,mapobject.wall((0,0,90),(90,0,90),5)
               ,mapobject.wall((0,5,95),(90,2,95),5)
               ,mapobject.wall((90,0,0),(90,0,100),10)
               ]
    

    return objects
