from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import character
import color
import bullet

class normalpot(character.enemy):
    normal_speed = 0.1
    dash_speed = 0.3
    v = normal_speed
    w = 5
    cameralock = False
    RTcounter = 0
    radius = 0.8

    def visual(self):
        if self.colornum == 0:
            color.gold()
        elif self.colornum == 1:
            color.red()
        glutSolidTeapot(1)
    
