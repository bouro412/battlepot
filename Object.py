from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import Color
import Character

class Bullet:
    speed = 0.5
    def __init__(self,position,vector):
        self.position = position
        self.vector = vector
    
    def visual(self):
        Color.green()
        glTranslate(1.5,0.5,0)
        glRotate(90,0,1,0)
        glutSolidCone(0.1,1,10,10)

    def forward(self):
        angle1 = cos(radians(self.vector[0]))
        angle2 = sin(radians(self.vector[0]))
        angle3 = cos(radians(self.vector[1]))
        angle4 = sin(radians(self.vector[1]))
        
        self.position[0] += angle3 * angle1 * self.speed
        self.position[1] += angle3 * angle2 * self.speed
        self.position[2] += angle4 * self.speed

    def draw(self):
        if self.vector[0] > 360:
            self.vector[0] += -360
        elif self.vector[0] < -360:
            self.vector[0] += 360
        vector = self.vector
        #self.gravity()
        glPushMatrix()

        glTranslatef(self.position[0],
                     self.position[1] + 0.7,
                     self.position[2])
        glRotate(vector[1], 
                 sin(radians(vector[0])), 
                 0,
                 cos(radians(vector[0])))
        glRotate(vector[0],0,1,0)
        self.visual()

        glPopMatrix()
