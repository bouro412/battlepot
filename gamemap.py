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
            print "Game Start"
            corner = [(-10,0,-40),(-10,0,40),(70,0,40),(70,0,-40)]
            box1 = [(50,0,-25),(60,0,-25),(60,0,-5),(50,0,-5)]
            box2 = [(50,4,20),(60,4,20),(60,4,30),(50,4,30)]
            box3 = [(60,0,16),(42,0,16),(42,0,30),(60,0,30)]
            box4 = [(10,0,0),(10,0,15),(40,0,15),(40,0,0)]
            objects[:] = [character.normalplayer(0, [0,0,0],[0,0,0],[0,25])
                          ,character.normalenemy(0,[30,0,-20],[180,0,0],[1,3])
                          ,character.normalenemy(2,[35,8,7],[180,0,0],[2,3])
                          ,character.normalenemy(1,[30,0,20],[180,0,0],[3,3])
                          ,mapobject.floor(corner[0],80,80)
                          ,mapobject.wall(corner[0],corner[1],80)
                          ,mapobject.wall(corner[1],corner[2],80)
                          ,mapobject.wall(corner[2],corner[3],80)
                          ,mapobject.wall(corner[3],corner[0],80)
                          ,mapobject.floor((50,4,-25),10,20)
                          ,mapobject.wall(box1[0],box1[1],4)
                          ,mapobject.wall(box1[1],box1[2],4)
                          ,mapobject.wall(box1[2],box1[3],4)
                          ,mapobject.wall(box1[3],box1[0],4)
                          ,mapobject.floor((50,14,20),10,10)
                          ,mapobject.wall(box2[0],box2[1],10)
                          ,mapobject.wall(box2[1],box2[2],10)
                          ,mapobject.wall(box2[2],box2[3],10)
                          ,mapobject.wall(box2[3],box2[0],10)
                          ,mapobject.floor((42,4,16),18,14)
                          ,mapobject.wall(box3[1],box3[2],4)
                          ,mapobject.wall(box3[1],box3[0],4)
                          ,mapobject.wall(box3[2],box3[3],4)
                          ,mapobject.wall(box3[3],box3[0],4)
                          ,mapobject.floor((10,8,0),30,15)
                          ,mapobject.wall(box4[0],box4[1],8)
                          ,mapobject.wall(box4[1],box4[2],8)
                          ,mapobject.wall(box4[2],box4[3],8)
                          ,mapobject.wall(box4[3],box4[0],8)
                          ]
            """
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
            

            ,mapobject.wall((-50,0,25),(-20,0,25),10)
            ,mapobject.wall((-20,0,25),(-20,0,75),10)
            ,mapobject.wall((-20,0,75),(-50,0,75),10)
            ,mapobject.floor((-50,10,25),30,50)
            """
                          
            
            self.start = True

        elif self.count_enemy(objects) == 0:
            self.wave += 1
            print "enemy0"
            print self.wave
            if objects[0].states[1] <= 15:
                objects[0].states[1] += 10
            else:
                objects[0].states[1] = 25
            if self.wave == 1:
                obj = [character.normalenemy(0,[0,0,20],[0,0,0],[4,3])
                       ,character.normalenemy(0,[0,0,30],[0,0,0],[5,3])]
                objects.extend(obj)
            elif self.wave == 2:
                obj = [character.normalenemy(0,[45,0,-30],[180,0,0],[6,4])
                       ,character.normalenemy(0,[45,0,-10],[180,0,0],[7,4])
                       ,character.normalenemy(1,[55,4,-15],[180,0,0],[8,4])]
                objects.extend(obj)
            elif self.wave == 3:
                obj = [character.normalenemy(0,[55,4,-20],[180,0,0],[4,5])
                       ,character.normalenemy(0,[55,4,-5],[180,0,0],[5,5])
                       ,character.normalenemy(0,[39,8,1],[180,0,0],[6,5])
                       ,character.normalenemy(1,[51,14,21],[180,0,0],[7,5])]
                
                objects.extend(obj)
            elif self.wave == 4:
                obj = [character.normalenemy(0,[20,8,1],[0,0,0],[8,5])
                       ,character.normalenemy(0,[30,8,1],[0,0,0],[9,5])
                       ,character.normalenemy(2,[8,0,-30],[0,0,0],[10,5])
                       ,character.normalenemy(2,[8,0,-10],[0,0,0],[11,5])]
                objects.extend(obj)
            elif self.wave == 5:
                obj = [character.bullenemy(0,[55,4,-20],[180,0,0],[12,6])
                       ,character.bullenemy(0,[55,4,-5],[180,0,0],[13,6])]
                objects.extend(obj)
            elif self.wave == 6:
                obj = [character.bullenemy(2,[30,8,7],[0,0,0],[14,7]),
                       character.bullenemy(2,[20,8,7],[180,0,0],[15,7])]
                objects.extend(obj)
            elif self.wave == 7:
                obj = [character.bullenemy(1,[52,14,23],[180,0,0],[16,8])
                       ,character.bullenemy(1,[52,14,26],[180,0,0],[17,8])]
                objects.extend(obj)
            elif self.wave == 8:
                obj = [character.bullenemy(0,[30,0,-30],[0,0,0],[18,6])
                       ,character.bullenemy(1,[10,0,-30],[0,0,0],[19,8])
                       ,character.bullenemy(2,[20,0,-15],[0,0,0],[20,7])]
                objects.extend(obj)
            elif self.wave >= 9:
                print "Game Clear!!"
                joyinput.quit()
                exit()
        if objects[0].states[1] <= 0:
            print "Game Over"
            joyinput.quit()
            exit()

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
