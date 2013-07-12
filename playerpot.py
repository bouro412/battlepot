from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Character
import pygame
from math import *

class normalpot(Character.player):
         
    
    def LeftAxis(self,Axis0,Axis1):
        move = 0
        if fabs(Axis0) > 0.3:
            self.side_move(-Axis0 * fabs(Axis0) * 0.2)
            move += 1
        if fabs(Axis1) > 0.3:
            self.strate_move(-Axis1 * fabs(Axis1) * 0.2)
            move += 1
        if move > 0:
            if fabs(Axis1) > 1:
                Axis1 = Axis1 / fabs(Axis1)
            if fabs(Axis0) > 1:
                Axis0 = Axis0 / fabs(Axis0)
            if Axis1 < 0:
                self.vector[0] = self.camera_angle[0] - degrees(asin(Axis0))
            elif Axis1 > 0:
                self.vector[0] = self.camera_angle[0] + degrees(asin(Axis0)) + 180.0
            else:
                self.vector[0] = self.camera_angle[0]

    def input(self,joyinput):
        axis = joyinput.axis
        buttons = joyinput.buttons
        self.LeftAxis(axis[0],axis[1])
        self.RightAxis(axis[3],axis[4])
