from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin ,cos,radians, fabs
import Color
import util
import Object
"""
colornum = int
position = x,y,z float * 3
vector = float * 2 in degrees
states = ?
camera_angle = float ? 2

"""
class character:
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
        #self.gravity()
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
        if isinstance(obj,Object.Bullet):
            pot = self.position
            after_bullet = obj.position
            before_bullet = obj.back()
            
            before_to_after = util.Vec(after_bullet) - util.Vec(before_bullet)
            pot_to_before = util.Vec(before_bullet) - util.Vec(pot)
            pot_to_after = util.Vec(after_bullet) - util.Vec(pot)

            if util.dot(before_to_after,-1 * pot_to_before) < 0:
                if util.norm(pot_to_before) < self.radius:
                    return True
                else: return False
            elif util.dot(before_to_after,pot_to_after) < 0:
                if util.norm(pot_to_after) < self.radius:
                    return True
                else: return False
            else:
                if util.norm(util.cross3d(before_to_after,pot_to_before)) / util.norm(before_to_after) < self.radius:
                    return True
                else: return False
            

        
        
class player(character):

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

    def input(self):
        pass
  
class enemy(character):
    def AI(self):
        pass

class testsphere(character):
    def visual(self):
        Color.green()
        glutSolidSphere(0.8,10,10)
