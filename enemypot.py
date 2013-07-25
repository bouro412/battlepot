from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Character
import Color
import Object

class normalpot(Character.enemy):
    normal_speed = 0.1
    dash_speed = 0.3
    v = normal_speed
    w = 5
    cameralock = False
    RTcounter = 0
    radius = 0.8

    def visual(self):
        if self.colornum == 0:
            Color.gold()
        elif self.colornum == 1:
            Color.red()
        glutSolidTeapot(1)
    
