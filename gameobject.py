# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin ,cos,radians, fabs
import color
import util

class gameobject:
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
position = [x,y,z] float3つで機体の座標を表す。 
vector = 機体の向き。float2つで初期の向きから左回転で水平方向の回転（yが軸）と縦方向の回転（機体の前方が軸）の角度をdegreesで表す
states = HPとか書きたい。未実装
camera_angle = float2つでカメラの向きを表す。表し方はvectorと同じ

"""
class character(gameobject):
    earth = 0.7
    radius = 0.8
    def __init__(self,colornum,position,vector
                 ,states,camera_angle = [0,0]):
        self.colornum = colornum
        self.vector = vector
        self.position = position
        self.states = states
        self.camera_angle = camera_angle

    def visual(self):
        pass
        
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
        self.position[0] += cos(radians(angle)) * distance
        self.position[2] += -sin(radians(angle)) * distance

    def side_move(self,distance):
        angle = self.camera_angle[0] + 90.0
        self.position[0] += cos(radians(angle)) * distance
        self.position[2] += -sin(radians(angle)) * distance

    def collision_detection(self,obj):
        """
        もともとcharacterクラス内で書かれていたので、
        selfはcharacterのインスタンスを指します。
        self.positionは長さ3のリストで（x座標、y座標,z座標）となります。
        self.earthはpotが地面にめり込まないための定数です。
        画面に表示する際はこの値だけself.positionのy座標にプラスして表示しているので、
        当たり判定でもそこを考慮して計算する必要がある。
        """
        if isinstance(obj,bullet.Bullet):
            pot = [self.position[0],
                   self.position[1] - self.earth,
                   self.position[2]]
            after_bullet = obj.position
            before_bullet = obj.back()
            
            before_to_after = util.Vec(after_bullet) - util.Vec(before_bullet)
            pot_to_before = util.Vec(before_bullet) - util.Vec(pot)
            pot_to_after = util.Vec(after_bullet) - util.Vec(pot)

            if util.dot(before_to_after,-1 * pot_to_before) < 0:
                if abs(pot_to_before) < self.radius:
                    return True
                else: return False
            elif util.dot(before_to_after,pot_to_after) < 0:
                if abs(pot_to_after) < self.radius:
                    return True
                else: return False
            else:
                if abs(util.cross3d(before_to_after,pot_to_before)) / abs(before_to_after) < self.radius:
                    return True
                else: return False
            

        
        
class player(character):
    def draw(self):
        self.camera()
        character.draw(self)
    
    def camera(self):
        angle = self.camera_angle
        eye = 1.75
        distance = 5.0
        fai = cos(radians(angle[1]))
        x = self.position[0]
        y = self.position[1] + eye
        z = self.position[2]
        glLoadIdentity()
        camera_position = [x - distance * cos(radians(angle[0]))*fai ,
                           y + distance * sin(radians(angle[1])) ,
                           z + distance * sin(radians(angle[0]))*fai]
        camera_vector = [x - camera_position[0],
                         y - camera_position[1],
                         z - camera_position[2]]
        gluLookAt(camera_position[0],
                  camera_position[1],
                  camera_position[2],
                  x,y,z,
                  0,1,0)

    def move(self):
        pass
  
class enemy(character):
    def AI(self):
        pass

