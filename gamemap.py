# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import character
import mapobject

def testmap():
    objects = [character.normalplayer(0, [-20,0,50],[0,0,0],[0,10])
               ,character.normalenemy(0,[10,0,50],[0,0,0],[1,10])
               ,character.normalenemy(1,[0,0,40],[0,0,0],[2,10])
               ,character.normalenemy(2,[0,0,60],[0,0,0],[2,10])
               #,mapobject.wall((0,0,0),(200,0,0),100)
               ,mapobject.floor((-50,0,0),150,100)
               ,mapobject.floor((0,10,0),90,10)
               ,mapobject.floor((0,5,10),90,10)
               ,mapobject.floor((0,5,80),90,10)
               ,mapobject.floor((0,10,90),90,10)
               ,mapobject.floor((80,10,0),20,100)
               ,mapobject.wall((-50,0,0),(-50,0,100),100)
               ,mapobject.wall((-50,0,0),(100,0,0),100)
               ,mapobject.wall((100,0,0),(100,0,100),100)
               ,mapobject.wall((-50,0,100),(100,0,100),100)
               ,mapobject.wall((0,0,20),(80,0,20),5)
               ,mapobject.wall((0,5,10),(80,5,10),5)
               ,mapobject.wall((0,0,80),(80,0,80),5)
               ,mapobject.wall((0,5,90),(80,2,90),5)
               ,mapobject.wall((80,0,0),(80,0,100),10)
               ,mapobject.wall((0,0,0),(0,0,10),10)
               ,mapobject.wall((0,0,10),(0,0,20),5)
               ,mapobject.wall((0,0,80),(0,0,90),5)
               ,mapobject.wall((0,0,90),(0,0,100),10)
               ]
    

    return objects
