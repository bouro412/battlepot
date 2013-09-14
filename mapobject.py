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

class wall(gameobject.gameobject):
    def __init__(self,base_point1,base_point2,
                 height,colornum=0,states=[-1,0]):
        self.base_point1 = util.Vec(base_point1)
        self.base_point2 = util.Vec(base_point2)
        self.height = height
        self.colornum = colornum
        self.states = states
        if self.base_point1[1] != self.base_point2[1]:
            self.base_point2 +=  (0,self.base_point1[1] - self.base_point2[1],0)
        vec1 = self.base_point2 - self.base_point1
        vec2 = util.Vec(0,1,0)

        normal = util.cross3d(vec1,vec2)
        self.normal = normal / abs(normal)
        
    def draw(self):
        coordinates = (self.base_point1
                       ,self.base_point1 + (0,self.height,0)
                       ,self.base_point2 + (0,self.height,0)
                       ,self.base_point2)

        color.yellow_plastic()
        glBegin(GL_QUADS)
        glNormal3fv(self.normal)
        for x in coordinates:
            glVertex3fv(x)
        glEnd()

    
