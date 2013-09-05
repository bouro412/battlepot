# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import util
import color
import gameobject

class floor(gameobject.gameobject):
    """
    floorは床オブジェクトで、接地のあたり判定のみを持つ。
    水平な長方形で表され、originからxにxlength、zにzlengthだけの長さの辺を持つ
    """
    def __init__(self,origin,xlength,zlength,
                 colornum=0,states = [-1,0]):
        self.origin = util.Vec(origin)
        self.xlength = xlength
        self.zlength = zlength
        self.colornum = colornum
        self.states = states
        self.height = origin[1]

    def draw(self):
        coordinates = [self.origin,
                       self.origin + (self.xlength,0,0),
                       self.origin + (self.xlength,0,self.zlength),
                       self.origin + (0,0,self.zlength)
                       ]

        color.yellow_plastic()
        glBegin(GL_QUADS)
        glNormal3f(0,1,0)
        for x in coordinates:
            glVertex3fv(x)
        glEnd()

