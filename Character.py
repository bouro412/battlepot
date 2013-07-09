from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin ,cos,radians

class character:
    def __init__(self,visual,position,vector,states):
        self.visual = visual
        self.vector = vector
        self.position = position
        self.states = states
    def draw(self):
        vector = self.vector
        glPushMatrix()

        glTranslatef(self.position[0],self.position[1] + 0.7,self.position[2])
        glRotate(vector[1], cos(radians(vector[0])), 0, -sin(radians(vector[0])))
        glRotate(vector[0],0,1,0)
        self.visual()

        glPopMatrix()
    def rotate(self,x,y):
        self.vector = [self.vector[0] + x,self.vector[1] + y]
    
    def move(self,distance):
        angle = self.vector[0]
        self.position[0] += cos(radians(angle)) * distance
        self.position[2] += -sin(radians(angle)) * distance

        
class player(character):
    def camera(self):
        angle = self.vector[0]
        x = self.position[0]
        y = self.position[2]
        glLoadIdentity()
        camera_position = [x -10 * cos(radians(angle))
                           ,2,y + 10 * sin(radians(angle))]
        camera_vector = [x - camera_position[0],0,y - camera_position[2]]
        gluLookAt(camera_position[0],camera_position[1],camera_position[2],
                  camera_position[0] + camera_vector[0] * 10,1,
                  camera_position[2] + camera_vector[2] * 10,
                  0,1,0)
    def input(self,ws,ad):
        if ws != 0:
            self.move(0.5 * ws)
        if ad != 0:
            self.rotate(3*ad,0)

        
