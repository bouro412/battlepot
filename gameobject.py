# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin ,cos,radians, fabs
import color
import util

class gameobject:
    __drawcancel = False
    __alive = True
    def draw(self):
        pass
    def isalive(self):
        return self.__alive
    def move(self,joy,objects):
        pass
    def kill(self):
        self.__alive = False

"""
colornum = intひとつ。機体の色を決めたい、未実装。
position = util.Vec([x,y,z]) float3つで機体の座標を表す。 
vector = 機体の向き。float2つで初期の向きから左回転で水平方向の回転（yが軸）と縦方向の回転（機体の前方が軸）の角度をdegreesで表す
states = [ID,HP]
camera_angle = float2つでカメラの向きを表す。表し方はvectorと同じ

"""
class character(gameobject):
    earth = 0.75
    radius = 0.8
    onearth = True
    before_onearth = True
    y_speed = 0
    fallspeed_limit = -30.0 / 60
    before_position = util.Vec(0,0,0)
    recovery = None

    def __init__(self,colornum,position,vector
                 ,states,camera_angle = [0,0]):
        self.colornum = colornum
        self.vector = vector
        self.position = util.Vec(position)
        self.states = states
        self.camera_angle = camera_angle

    def visual(self):
        pass
    def move(self,joy,objects):
        self.before_position = self.position
        if self.y_speed >= self.fallspeed_limit:
            self.position += (0,self.y_speed,0)
        else:
            self.position += (0,self.fallspeed_limit,0)
        self.gravity()
        if not self.before_onearth and self.onearth and self.recovery == None:
            self.recovery = [self.landing,100,1]
        self.before_onearth = self.onearth
        
    def draw(self):
        if self.vector[0] > 360:
            self.vector[0] += -360
        elif self.vector[0] < -360:
            self.vector[0] += 360
        vector = self.vector
        glPushMatrix()

        glTranslatef(self.position[0],
                     self.position[1] + self.earth,
                     self.position[2])
        glRotate(vector[2]
                 ,cos(radians(vector[0]))
                 ,0
                 ,-sin(radians(vector[0])))
        glRotate(vector[1], 
                 sin(radians(vector[0])), 
                 0,
                 cos(radians(vector[0])))
        glRotate(vector[0],0,1,0)
        self.visual()
        glPopMatrix()
    def rotate(self,x,y):
        self.vector = [self.vector[0] + x,self.vector[1] + y]
    
    def strate_move(self,distance):
        angle = self.vector[0]
        self.position += (cos(radians(angle)) * distance
                          ,0
                          ,-sin(radians(angle)) * distance)

    def side_move(self,distance):
        angle = self.camera_angle[0] + 90.0
        self.position  += (cos(radians(angle)) * distance
                           ,0
                           ,-sin(radians(angle)) * distance)

    def damage(self,damage):
        if self.states[1] > 0:
            self.states[1] -= damage
    def gravity(self):
        if not self.onearth:
            self.y_speed -= 60.0 / 3600
    def jump(self):
        self.y_speed = 20.0 / 60
        self.position += (0,20.0/60,0)
    def landing(self,count,no_use,joyinput,objects):
        if count < 0:
            self.recovery = None
        
class player(character):
    camera_position = util.Vec(0,0,0)
    
    def draw(self):
        self.camera()
        character.draw(self)
    
    def camera(self):
        angle = self.camera_angle
        eye = 1.75
        distance = 8.0
        fai = cos(radians(angle[1]))
        x = self.position[0]
        y = self.position[1] + eye
        z = self.position[2]
        glLoadIdentity()
        self.camera_position = util.Vec(
            [x - distance * cos(radians(angle[0]))*fai ,
             y + distance * sin(radians(angle[1])) ,
             z + distance * sin(radians(angle[0]))*fai])
        camera_vector = [x - self.camera_position[0],
                         y - self.camera_position[1],
                         z - self.camera_position[2]]
        gluLookAt(self.camera_position[0],
                  self.camera_position[1],
                  self.camera_position[2],
                  x,y,z,
                  0,1,0)

    
  
class enemy(character):
    def AI(self):
        pass
    def rotate(self,x,y):
        self.vector = [self.vector[0] + x,self.vector[1] + y]
    def move(self,joy,objects):
        character.move(self,joy,objects)
        if self.states[1] <= 0:
            self.kill()
        

    

        
