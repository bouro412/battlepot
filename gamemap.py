# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import character
import mapobject
import gameobject

class Map:
    start = False
    wave = 0
    def __init__(self,number):
        self.number = number
    def move(self,joyinput,objects):
        if self.number == 0:
            self.stage1_move(joyinput,objects)

    def stage1_move(self,joyinput,objects):    
        if self.start == False:
            print "start"
            objects[:] = [character.normalplayer(0, [-20,0,50],[0,0,0],[0,25])
                          ,character.normalenemy(0,[10,0,50],[180,0,0],[1,5])
                          ,character.normalenemy(1,[0,0,40],[180,0,0],[2,5])
                          ,character.normalenemy(2,[0,0,60],[180,0,0],[3,5])
                          ,mapobject.floor((-50,0,0),150,100)
                          ,mapobject.floor((0,10,0),90,10)
                          ,mapobject.floor((0,5,10),90,10)
                          ,mapobject.floor((0,5,80),90,10)
                          ,mapobject.floor((0,10,90),90,10)
                          ,mapobject.floor((80,10,0),20,100)
                          ,mapobject.floor((-50,100,0),150,100)
                          ,mapobject.wall((-50,0,0),(-50,0,100),100)
                          ,mapobject.wall((-50,0,0),(100,0,0),100)
                          ,mapobject.wall((100,0,0),(100,0,100),100)
                          ,mapobject.wall((-50,0,100),(100,0,100),100)
                          ,mapobject.wall((0,0,20),(80,0,20),5)
                          ,mapobject.wall((0,5,10),(80,5,10),5)
                          ,mapobject.wall((0,0,80),(80,0,80),5)
                          ,mapobject.wall((0,5,90),(80,2,90),5)
                          ,mapobject.wall((80,0,0),(80,0,100),10)
                          ,mapobject.wall((0,0,0),(0,0,10),10)
                          ,mapobject.wall((0,0,10),(0,0,20),5)
                          ,mapobject.wall((0,0,80),(0,0,90),5)
                          ,mapobject.wall((0,0,90),(0,0,100),10)
                          ]
            
            self.start = True

        elif self.count_enemy(objects) == 0:
            print "enemy0"
            if self.wave == 0:
                self.wave += 1
                obj = [character.normalenemy(0,[50,0,50],[180,0,0],[4,5])
                       ,character.normalenemy(1,[15,5,10],[180,0,0],[5,5])
                       ,character.normalenemy(2,[15,5,40],[180,0,0],[6,5])]
                objects.extend(obj)
                """obj = character.normalenemy(0,[50,0,50],[180,0,0],[4,5])
                objects.append(obj)"""
            
    def stage_end(self):
        self.start = False
        self.wave = 0
    def count_enemy(self,objects):
        count = 0
        for x in objects:
            if isinstance(x,gameobject.enemy):
                count += 1
        return count

def testmap():
    objects = [character.normalplayer(0, [-20,0,50],[0,0,0],[0,25])
               ,character.normalenemy(0,[10,0,50],[0,0,0],[1,5])
               ,character.normalenemy(1,[0,0,40],[0,0,0],[1,5])
               ,character.normalenemy(2,[0,0,60],[0,0,0],[1,5])
               #,mapobject.wall((0,0,0),(200,0,0),100)
               ,mapobject.wall((-50,0,0),(-50,0,100),100)
               ,mapobject.wall((-50,0,0),(100,0,0),100)
               ,mapobject.wall((100,0,0),(100,0,100),100)
               ,mapobject.wall((-50,0,100),(100,0,100),100)
               ,mapobject.wall((0,0,20),(80,0,20),5)
               ,mapobject.wall((0,5,10),(80,5,10),5)
               ,mapobject.wall((0,0,80),(80,0,80),5)
               ,mapobject.wall((0,5,90),(80,2,90),5)
               ,mapobject.wall((80,0,0),(80,0,100),10)
               ,mapobject.wall((0,0,0),(0,0,10),10)
               ,mapobject.wall((0,0,10),(0,0,20),5)
               ,mapobject.wall((0,0,80),(0,0,90),5)
               ,mapobject.wall((0,0,90),(0,0,100),10)
               ,mapobject.floor((-50,0,0),150,100)
               ,mapobject.floor((0,10,0),90,10)
               ,mapobject.floor((0,5,10),90,10)
               ,mapobject.floor((0,5,80),90,10)
               ,mapobject.floor((0,10,90),90,10)
               ,mapobject.floor((80,10,0),20,100)

               ]
    

    return objects
