# -*- coding: utf-8 -*-

"""
このファイルで定義されているのはすべて抽象クラスです。
実体はplayerpot,enemypotで定義される。
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin ,cos,radians, fabs, degrees, atan,asin,acos,pi,sqrt
import copy
import color
import util
import bullet
import gameobject

class normalplayer(gameobject.player):

    normal_speed = 0.1
    dash_speed = 0.3
    v = normal_speed
    w = 5
    cameralock = False
    normal_camera_speed = 2.0
    slow_camera_speed = 0.7
    camera_speed = normal_camera_speed
    RTcounter = 0
    recovery = None
    radius = 0.8
    slip = util.Vec(0,0,0) 
    friction = 0.01
    
    def visual(self):
        if self.colornum == 0:
            color.gold()
        glutSolidTeapot(1)

    def move(self,joyinput,objects):
        axis = joyinput.axis
        buttons = joyinput.buttons
        add_objects = []

        self.RightAxis(joyinput)
        self.LB(joyinput)
        self.slipmove()

        if self.recovery != None:
            self.recovery[1] += -17
            self.recovery[0](self.recovery[1],self.recovery[2],
                             joyinput,objects)
            return 0
            
        self.LT(joyinput)
        self.LeftAxis(joyinput)
        if self.RTcounter > 0:
            self.RTshotrecharge()
        else:
            ob = self.RTshot(joyinput)
            if ob != None:
                objects.append(ob)
   
    def RightAxis(self,joyinput):
        Axis3 = joyinput.axis[3]
        Axis4 = joyinput.axis[4]
        if fabs(Axis3) > 0.2:
            self.camera_angle[0] += -Axis3 * self.camera_speed
            if self.camera_angle[0] >= 360:
                self.camera_angle[0] += -360.0
            elif self.camera_angle[0] <= -360:
                self.camera_angle[0] += 360
            if self.cameralock:
                self.vector[0] = self.camera_angle[0]
                self.camera_speed = self.slow_camera_speed
            else:
                self.camera_speed = self.normal_camera_speed
        if fabs(Axis4) > 0.2:
            if Axis4 < 0:
                if self.camera_angle[1] > -80:
                    self.camera_angle[1] += Axis4 * self.camera_speed
            elif Axis4 > 0:
                if self.camera_angle[1] < 80:
                    self.camera_angle[1] += Axis4 * self.camera_speed
    #"""
    def LeftAxis(self,joyinput):
        Axis0 = joyinput.axis[0]
        Axis1 = joyinput.axis[1]
        if self.cameralock == True:
            if fabs(Axis0) > 0.3:
                self.side_move(-Axis0 * fabs(Axis0) * self.v * 0.8)
            if fabs(Axis1) > 0.3:
                self.strate_move(-Axis1 * fabs(Axis1) * self.v * 0.8)
        else:
            if fabs(Axis1) > 0.3 or fabs(Axis0) > 0.3:
                self.strate_move((Axis0 ** 2 + Axis1 ** 2) * self.v)
                self.rotate_move_direction(joyinput)
    

    def rotate_move_direction(self,joyinput):
        Axis0 = joyinput.axis[0]
        Axis1 = joyinput.axis[1]
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
            

 

    def LT(self,joyinput):
        axis = joyinput.axis
        if axis[2] > 0:
            if self.cameralock:
                self.recovery = [self.LTstep,300,copy.deepcopy(axis)]
            else:
                self.recovery = [self.LTboost,300,copy.deepcopy(axis)]
            
        """
        if self.cameralock == False and Axis2 > 0:
                self.vector[1] = -20
                self.v = self.dash_speed
                self.w = 1
        else:
            self.vector[1] = 0
            self.v = self.normal_speed
            self.w = 5
            """
    def LTstep(self,count,axis,joyinput,objects):
        if count > 0:
            v = (count / 150) ** 2 + 0.15 
            if axis[1] < -0.5:
                self.vector[1] = -10
                self.strate_move(v)
            elif axis[1] > 0.5:
                self.vector[1] = 10
                self.strate_move(-v)
            elif axis[0] < -0.5:
                self.side_move(v)
                self.vector[2] = -10
            elif axis[0] > 0.5:
                self.side_move(-v)
                self.vector[2] = 10
            else:
                self.recovery = None
        else:
            self.recovery = None
            self.vector[1] = 0
            self.vector[2] = 0
            

    def LTboost(self,count,axis,joyinput,objects):
        if count < 0:
            if axis[2] > 0:
                self.recovery = [self.boost_persist,1,axis]
            else:
                self.vector[1] = 0
                self.recovery = None
                return

        if axis[0] ** 2 + axis[1] ** 2 < 0.5:
            self.strate_move(1.0)
            self.vector[1] = -10
            return
        elif axis[0] == 0:
            LeftStickAngle = 90 * (-axis[1] / fabs(axis[1]))
        else:
            LeftStickAngle = degrees(atan(-axis[1] / axis[0]))
        if axis[0] < 0:
            LeftStickAngle += 180

            
        if LeftStickAngle < -67.5 or LeftStickAngle > 247.5:
            self.vector = [self.camera_angle[0] + 180, -10, 0]
        elif LeftStickAngle < -22.5:
            self.vector = [self.camera_angle[0] - 135, -10, 0]
        elif LeftStickAngle < 22.5:
            self.vector = [self.camera_angle[0] - 90, -10, 0]
        elif LeftStickAngle < 67.5:
            self.vector = [self.camera_angle[0] - 45, -10 ,0]
        elif LeftStickAngle < 112.5:
            self.vector = [self.camera_angle[0] , -10, 0]
        elif LeftStickAngle < 157.5:
            self.vector = [self.camera_angle[0] + 45, -10, 0]
        elif LeftStickAngle < 202.5:
            self.vector = [self.camera_angle[0] +90, -10, 0]
        elif LeftStickAngle < 247.5:
            self.vector = [self.camera_angle[0] + 135, -10, 0] 

        self.strate_move(1.0)
        
    def boost_persist(self,count,axis,joyinput,objects):
        Axis2 = joyinput.axis[2]
        #self.cameralock = False
        if Axis2 > 0:
            self.vector[1] = -10
            self.v = self.dash_speed
            self.w = 1
            self.LeftAxis(joyinput)
            if self.RTcounter > 0:
                self.RTshotrecharge()
            else:
                ob = self.RTshot(joyinput)
                if ob != None:
                    objects.append(ob)
            
        else:
            self.vector[1] = 0
            self.v = self.normal_speed
            self.w = 5
            self.recovery = None

    def LB(self,joyinput):
        Button4 = joyinput.buttons[4]
        if Button4 == 1:
            self.vector[0] = self.camera_angle[0]
            self.cameralock = True
        if Button4 == -1:
            self.cameralock = False

    def RTshot(self,joyinput):
        Axis5 = joyinput.axis[5]
                       
        if Axis5 > 0:
            posi = copy.deepcopy(self.position)
            vec = copy.deepcopy(self.camera_angle)
            vec[1] = -vec[1]
            posi += (1.5 * cos(radians(self.vector[0]))
                     ,0
                     ,1.5 * -sin(radians(self.vector[0])))
            
            result = bullet.Bullet(posi,vec,[self.states[0],1])
            self.RTshotrecharge()
            return result
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
    def slipmove(self):
        self.position += self.slip
        level_slip = util.Vec(self.slip[0],0,self.slip[2])
        if abs(level_slip) < self.friction:
            self.slip -= level_slip
        else:
            self.slip -= level_slip * self.friction / abs(level_slip)

    def jump(self,joyinput):
        pass

class normalenemy(gameobject.enemy):
    normal_speed = 0.1
    dash_speed = 0.3
    v = normal_speed
    w = 5
    cameralock = False
    shot_counter = 0
    radius = 0.8
    before_player_position = None

    def visual(self):
        if self.colornum == 0:
            color.gold()
        elif self.colornum == 1:
            color.red()
        glutSolidTeapot(1)

    def to_player_angles(self,player_position):
        vector = util.Vec(player_position) - util.Vec(self.position)
        vector = vector / abs(vector)
        theta1 = asin(vector[1])
        theta0 = atan((vector[2] / cos(theta1)) / -(vector[0] / cos(theta1)))
        if vector[0] < 0:
            theta0 += pi
        angle = [degrees(theta0),degrees(theta1)]
        return angle
    
    def rotate_player_direction(self,player_angle):
        vector = player_angle
        distance = [0,0]
        for x in range(2):
            if vector[x] > 360:
                vector += -360
            elif vector[x] < 0:
                vector[x] += 360
            distance[x] = vector[x] - self.vector[x]
            if distance[x] < -180:
                distance[x] += 360
            elif distance[x] > 180:
                distance[x] += -360
            if fabs(distance[x]) <= self.w:
                self.vector[x] = vector[x]
            else:
                if distance[x] > 0:
                    self.vector[x] += self.w
                else:
                    self.vector[x] += -self.w
    
    def move(self,joy,objects):
        player_angle = self.to_player_angles(objects[0].position)
        self.rotate_player_direction(player_angle)
        if self.shot_counter > 0:
            self.shot_recharge()
        else:
            ob = self.hensa_shot(objects)
            if ob != 0:
                objects.append(ob)

    def shot_player(self,player_angle,bullet_type):
        posi = copy.deepcopy(self.position)
        vec = player_angle
        vec[1] = -vec[1]
        posi += (1.5 * cos(radians(self.vector[0]))
                 ,0
                 ,1.5 * -sin(radians(self.vector[0])))
            
        if bullet_type == 0:
            result = bullet.Bullet(posi,vec,[self.states[0],1])
        if bullet_type == 1:
            result = bullet.guided_bullet(posi, vec,[self.states[0],1])
        self.shot_recharge()
        return result

    def hensa_shot(self,objects):
        player = objects[0]
        if self.before_player_position == None:
            self.before_player_position = copy.deepcopy(player.position)
            return 0
        else:
            player_move = player.position - self.before_player_position
            bullet_speed = 3.0
            player_speed = abs(player_move)
            to_player = player.position - self.position
            
            a = player_speed ** 2 - bullet_speed ** 2
            b = util.dot(player_move , to_player)
            c = abs(to_player) ** 2

            t = (b - sqrt(b ** 2 - a * c)) / a
            target = player.position + player_move * t
            self.before_player_position = None
            return self.shot_player(self.to_player_angles(target),0)
    
    def shot_recharge(self):
        self.shot_counter += 17
        if self.shot_counter >= 1000:
            self.shot_counter = 0
            
