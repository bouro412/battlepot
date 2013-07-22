from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Character
import pygame
from math import *
import copy
import Color
import Object
import time
import util
normal_speed = 0.1
dash_speed = 0.3

class normalpot(Character.player):

    v = normal_speed
    w = 5
    cameralock = False
    RTcounter = 0
         
    def visual(self):
        if self.colornum == 0:
            Color.gold()
        glutSolidTeapot(1)

    def input(self,joyinput):
        axis = joyinput.axis
        buttons = joyinput.buttons
        add_objects = []
        
        self.LTboost(axis[2]) 
        self.LeftAxis(axis[0],axis[1])
        self.RightAxis(axis[3],axis[4])
        self.LB(buttons[4])
        if self.RTcounter > 0:
            self.RTshotrecharge()
        else:
            ob = self.RTshot(axis[5])
            if ob != None:
                add_objects.append(ob)
        
        return add_objects
   
    def RightAxis(self,Axis3,Axis4):
        if fabs(Axis3) > 0.3:
            self.camera_angle[0] += -Axis3 * 2
            if self.camera_angle[0] >= 360:
                self.camera_angle[0] += -360.0
            elif self.camera_angle[0] <= -360:
                self.camera_angle[0] += 360
            if self.cameralock:
                self.vector[0] = self.camera_angle[0]
        if fabs(Axis4) > 0.3:
            if Axis4 < 0:
                if self.camera_angle[1] > -80:
                    self.camera_angle[1] += Axis4 * 1.5
            elif Axis4 > 0:
                if self.camera_angle[1] < 80:
                    self.camera_angle[1] += Axis4 * 1.5
    #"""
    def LeftAxis(self,Axis0,Axis1):
        if self.cameralock == True:
            if fabs(Axis0) > 0.3:
                self.side_move(-Axis0 * fabs(Axis0) * self.v * 0.8)
            if fabs(Axis1) > 0.3:
                self.strate_move(-Axis1 * fabs(Axis1) * self.v * 0.8)
        else:
            if fabs(Axis1) > 0.3 or fabs(Axis0) > 0.3:
                self.strate_move((Axis0 ** 2 + Axis1 ** 2) * self.v)
                self.rotate_move_direction(Axis0,Axis1)
    

    def rotate_move_direction(self,Axis0,Axis1):
        if fabs(Axis1) > 1:
            Axis1 = Axis1 / fabs(Axis1)
        if fabs(Axis0) > 1:
            Axis0 = Axis0 / fabs(Axis0)
        if Axis1 < 0:
            vector = self.camera_angle[0] + degrees(atan(Axis0 / Axis1))
        elif Axis1 > 0:
            vector = self.camera_angle[0] + degrees(atan(Axis0 / Axis1)) + 180.0
        else:
            if Axis0 > 0:
                vector = self.camera_angle[0] - 90
            else:
                vector = self.camera_angle[0] + 90
        if vector > 360:
            vector += -360
        elif vector < 0:
            vector += 360
        distance = vector - self.vector[0]
        if distance < -180:
            distance += 360
        elif distance > 180:
            distance += -360
        if fabs(distance) <= self.w:
            self.vector[0] = vector
        else:
             if distance > 0:
                self.vector[0] += self.w
             else:
                self.vector[0] += -self.w
            

 

    def LTboost(self,Axis2):
        if self.cameralock == False and Axis2 > 0:
                self.vector[1] = 5
                self.v = dash_speed
                self.w = 1
        else:
            self.vector[1] = 0
            self.v = normal_speed
            self.w = 5
         
    
    def LB(self,Button4):
        if Button4 ==1:
            self.vector[0] = self.camera_angle[0]
            self.cameralock = True
        if Button4 == -1:
            self.cameralock = False

    def RTshot(self,Axis5):
        #if not cameralock:
                       
        if Axis5 > 0:
            posi = copy.deepcopy(self.position)
            vec = copy.deepcopy(self.camera_angle)
            pot_vec = copy.deepcopy(self.vector)
            vec[1] = -vec[1]
            posi[0] += 1.5 * cos(radians(self.vector[0]))
            posi[2] += 1.5 * -sin(radians(self.vector[0]))
            
            bullet = Object.Bullet(posi,vec,pot_vec)
            self.RTshotrecharge()
            return bullet
        else:
            return None
            
    def RTshotrecharge(self):
        self.RTcounter += 17
        if self.cameralock:
            if self.RTcounter >= 100:
                self.RTcounter = 0
        else:
            if self.RTcounter >= 300:
                self.RTcounter = 0

    def collision_detection(obj):
        if isinstance(obj,Object.Bullet):
            pot = self.position
            after_bullet = obj.position
            before_bullet = obj.back()
            
            before_to_after = util.Vec(after_bullet) - util.Vec(before_bullet)
            pot_to_before = util.Vec(before_bullet) - util.Vec(pot)
            pot_to_after = util.Vec(after_bullet) - util.Vec(pot)

            if util.dot(before_to_after,-1 * pot_to_before) < 0:
                if util.norm(pot_to_before) < 0.8:
                    return True
                else: return False
            elif util.dot(before_to_after,pot_to_after) < 0:
                if util.norm(pot_to_after) < 0.8:
                    return True
                else: return False
            elif:
                if util.norm(util.cross3d(before_to_after,pot_to_before)) / util.norm(before_to_after) < 0.8:
                    return True
                else: return False
            
                
