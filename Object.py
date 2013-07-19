from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import Color
import Character

class Bullet:
    speed = 10.0
    timelimit = 3000
    time = 0
    def __init__(self,position,vector,pot_vector):
        self.position = position
        self.vector = vector
        self.pot_vector = pot_vector
    
    def visual(self):
        Color.green()
        #glTranslate(1.5,0.5,0)
        glRotate(90 + self.vector[0],0,1,0)
        glRotate(-self.vector[1],1,0,0)
        #glRotate(90,0,1,0)
        glutSolidCone(0.2,1,10,10)

    def forward(self):
        angle1 = cos(radians(self.vector[0]))
        angle2 = sin(radians(self.vector[0]))
        angle3 = cos(radians(self.vector[1]))
        angle4 = sin(radians(self.vector[1]))
        
        #"""
        self.position[0] += angle3 * angle1 * self.speed
        self.position[1] += angle4 *  self.speed
        self.position[2] += -angle3 * angle2 * self.speed 
        """

        self.position[0] += angle1 * self.speed
        self.position[2] += -angle2 * self.speed
        """
    def draw(self):
        if self.vector[0] > 360:
            self.vector[0] += -360
        elif self.vector[0] < -360:
            self.vector[0] += 360
        vector = self.pot_vector
        #self.forward()
        glPushMatrix()

        glTranslatef(self.position[0],
                     self.position[1] + 1.2,
                     self.position[2])
        """
        glRotate(vector[1], 
                 sin(radians(vector[0])), 
                 0,
                 cos(radians(vector[0])))
        glRotate(vector[0],0,1,0)"""
        self.visual()

        glPopMatrix()

        self.time += 17
        #self.forward()

    def fadeout(self):
        if self.time >= self.timelimit:
            return True
        else:
            False
