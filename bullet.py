# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import color
import util
import gameobject



class Bullet(gameobject.gameobject):
    speed = 3.0
    timelimit = 1000
    

    def __init__(self,position,vector,states):
        self.position = util.Vec(position)
        self.vector = vector
        self.states = states
        self.before_position = util.Vec(position) - (0,0,0.0000001)
        #statesは[ID,damage]のリスト
    
    def visual(self):
        color.green()
        glRotate(90 + self.vector[0],0,1,0)
        glRotate(-self.vector[1],1,0,0)
        glutSolidCone(0.2,1,10,10)

    def move(self,joy,objects):
        self.before_position = self.position
        angle1 = cos(radians(self.vector[0]))
        angle2 = sin(radians(self.vector[0]))
        angle3 = cos(radians(self.vector[1]))
        angle4 = sin(radians(self.vector[1]))
        
        self.position += (angle3 * angle1 * self.speed
                          ,angle4 *  self.speed
                          , -angle3 * angle2 * self.speed) 

    def draw(self):
        if self.vector[0] > 360:
            self.vector[0] += -360
        elif self.vector[0] < -360:
            self.vector[0] += 360

        glPushMatrix()
        glTranslatef(self.position[0],
                     self.position[1] + 1.2,
                     self.position[2])
        self.visual()
        glPopMatrix()

        self.timelimit += -17


    def isalive(self):
        return gameobject.gameobject.isalive(self) and\
            self.timelimit > 0

class guided_bullet(Bullet):
    speed = 1.5
    timelimit = 3000
    w = 1.5
    def to_player_angles(self,player):
        vector = player.position - self.position
        vector = vector / abs(vector)
        theta1 = asin(vector[1])
        theta0 = atan((vector[2] / cos(theta1)) / -(vector[0] / cos(theta1)))
        if vector[0] < 0:
            theta0 += pi
        angle = [degrees(theta0),degrees(theta1)]
        return angle

    def guidance(self,player):
        angle = self.to_player_angles(player)
        distance = [0,0]
        for x in range(2):
            if angle[x] > 360:
                angle += -360
            elif angle[x] < 0:
                angle[x] += 360
            distance[x] = angle[x] - self.vector[x]
            if distance[x] < -180:
                distance[x] += 360
            elif distance[x] > 180:
                distance[x] += -360
            if fabs(distance[x]) <= self.w:
                self.vector[x] = angle[x]
            else:
                if distance[x] > 0:
                    self.vector[x] += self.w
                else:
                    self.vector[x] += -self.w
    
    def move(self,joy,objects):
        self.guidance(objects[0])
        Bullet.move(self,joy,objects)
        

class fast_bullet(Bullet):
    speed = Bullet.speed * 2
