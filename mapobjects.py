# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import util
import gameobject

class floor(gameobject.gameobject):
    def __init__(self,coordinates4,colornum=0):
        self.coordinate4 = [util.Vec(x) for x in coordinate4]
        self.colornum = colornum

    def draw(self):
        color.yellow_plastic()
        glBegin(GL_QUADS)
        glnormal3f(0,1,0)
        for x in self.coordinate4:
            glVertex3fv(x)
        glEnd()
