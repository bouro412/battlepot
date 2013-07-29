from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

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
