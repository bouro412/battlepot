# -*- coding: utf-8 -*-

"""
メインルーチンはこの中のdraw関数で定義されている。
step内のやりとりはこの中で別の関数にまとめたい。
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import color
import gameobject
import character
import bullet
import mapobject
import util
hitcount = 0
     
def step(objects,joy):
     global hitcount
     #描画設定の初期化
     glMatrixMode(GL_MODELVIEW)
     glClearColor(0,1,1,1)
     glClearDepth(1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glEnable(GL_DEPTH_TEST)
     glEnable(GL_COLOR_MATERIAL)
     
     light()  
     #ジョイスティックの読み取り
     joy.input()
 
     #オブジェクトの移動
     for ob in objects[:]:
          ob.move(joy,objects)
          
     #衝突判定
     for i in range(len(objects)-1):
          for j in range(i+1,len(objects)):
               collision_detection(objects[i],objects[j])

                        
    #オブジェクトの削除
     # objects = [x for x in objects if x.isalive()]
     for i, obj in reversed( tuple( enumerate( objects ) ) ):
          if not obj.isalive():
               del objects[ i ]

     #オブジェクトの描画
     for ob in objects:
          ob.draw()

     color.yellow_plastic()
     glBegin(GL_QUADS)
     glNormal3f(0,1,0)
     glVertex3f(0,0,0)
     glVertex3f(100,0,0)
     glVertex3f(100,0,100)
     glVertex3f(0,0,100)
     glEnd()

     draw2D(objects)
          
     #描画の後処理
     glDisable(GL_COLOR_MATERIAL)
     glDisable(GL_DEPTH_TEST)
     glutSwapBuffers()

#光源設定。毎回呼ばれる
def light():
    lightamb = [0,0,0,1]
    lightdiff = [1,1,1,1]
    lightspe = [1,1,1,1]
    lightpos = [1,1,1,0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, lightamb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightdiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightspe)

    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)

    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

def draw2D(objects):
     glMatrixMode(GL_PROJECTION)
     glPushMatrix()
     glLoadIdentity()
     gluOrtho2D(0, 640, 0, 480)
     #MODELVIEW行列を操作
     glMatrixMode(GL_MODELVIEW) 
     glPushMatrix() #MODELVIEW行列を保存
     glLoadIdentity()
     #いろいろ無効にする
     glDisable(GL_DEPTH_TEST)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
     #描画
     glBegin(GL_QUADS)
     glColor(0,0,0,1)
     glVertex2f(10,460)
     glVertex2f(10,430)
     glVertex2f(400,430)
     glVertex2f(400,460)
     glEnd()

     playerHP = objects[0].states[1]
     glBegin(GL_QUADS)
     glColor(0,1,0,1)
     glVertex2f(10,460)
     glVertex2f(10,430)
     glVertex2f(10 + playerHP * 39 ,430)
     glVertex2f(10 +playerHP * 39,460)
     glEnd()

     glBegin(GL_LINES)
     glColor(1,1,1,1)
     glVertex2f(320,230)
     glVertex2f(320,240)
     glVertex2f(315,235)
     glVertex2f(325,235)
     glEnd()

     #元に戻す（3D用へ戻る）
     glEnable(GL_DEPTH_TEST)
     glEnable(GL_LIGHTING)
     glEnable(GL_LIGHT0)
     glPopMatrix() #MODELVIEW行列をもとに戻す
     glMatrixMode(GL_PROJECTION) 
     glPopMatrix() #PROJECTION行列をもとに戻す


def collision_detection(obj1,obj2):
     """
     もともとcharacterクラス内で書かれていたので、書き直す必要がある。
     selfはcharacterのインスタンスを指します。
     self.positionは長さ3のリストで（x座標、y座標,z座標）となります。
     self.earthはpotが地面にめり込まないための定数です。
     画面に表示する際はこの値だけself.positionのy座標にプラスして表示しているので、
     当たり判定でもそこを考慮して計算する必要がある。
     """
     if isinstance(obj1,gameobject.character):
          if isinstance(obj2,bullet.Bullet):
               if chara_and_bullet(obj1,obj2):
                    obj1.damage(obj2.states[1])
                    obj2.kill()
          elif isinstance(obj2,gameobject.character):
               chara_and_chara_ALL(obj1,obj2)
          elif isinstance(obj2,mapobject.floor):
               result =  chara_and_floor(obj1,obj2)
               if result == 1:
                    obj1.y_speed = 0
                    obj1.onearth = True
               elif result == 0:
                    obj1.onearth = False
               else:
                    pass
     elif isinstance(obj1,bullet.Bullet):
          if isinstance(obj2,gameobject.character):
               if chara_and_bullet(obj1,obj2):
                    obj2.damage(obj1.states[1])
                    obj1.kill()
          elif isinstance(obj2,mapobject.floor):
               if bullet_and_floor(obj1,obj2):
                    obj1.kill()
     elif isinstance(obj1,mapobject.floor):
          if isinstance(obj2,gameobject.character):
               result = chara_and_floor(obj2,obj1)
               if result == 1:
                    obj2.y_speed = 0
                    obj2.onearth = True
               elif result == 0:
                    obj2.onearth = False
               else:
                    pass
          elif isinstance(obj2,bullet.Bullet):
               if bullet_and_floor(obj2,obj1):
                    obj2.kill()
                    
        
def chara_and_bullet(chara,bullet):
     if chara.states[0] == bullet.states[0]:
             return False
     pot = chara.position - (0,chara.earth,0)
     after_bullet = bullet.position
     before_bullet = bullet.before_position
            
     before_to_after = after_bullet - util.Vec(before_bullet)
     pot_to_before = util.Vec(before_bullet) - util.Vec(pot)
     pot_to_after = util.Vec(after_bullet) - util.Vec(pot)

     if util.dot(before_to_after,-1 * pot_to_before) < 0:
          return abs(pot_to_before) < chara.radius
     elif util.dot(before_to_after,pot_to_after) < 0:
          return abs(pot_to_after) < chara.radius
     else:
          return abs(util.cross3d(before_to_after,pot_to_before)) / abs(before_to_after) < chara.radius

def chara_and_floor(chara,floor):
     """
     キャラクターと地面との判定
     着地時は1を、してないときは0を、
     そもそもxz的に平面上にないとき、または平面の下にいるとき-1を返す
     """
     if chara.position[0] >= floor.origin[0] and chara.position[0] < floor.origin[0] + floor.xlength and chara.position[2] >= floor.origin[2] and chara.position[2] < floor.origin[2] + floor.zlength:
          if chara.before_position[1] >= chara.position[1]:
               if chara.before_position[1] >= floor.height and chara.position[1] <= floor.height:
                    chara.position += (0,floor.height - chara.position[1],0)
                    return 1
               else:
                    return 0
          else:
               if chara.before_position[1] >= floor.height:
                    return 0
               elif chara.position[1] + 1.6 >= floor.height:
                    chara.y_speed = 0
                    chara.position += (0,floor.height - chara.position[1] -1.6,0)
                    return -1
               else:
                    return -1
                    
     else:
          return -1

def chara_and_chara_ALL(chara1,chara2):
     distance = abs(chara1.position - chara2.position)
     if distance < chara1.radius + chara2.radius:
          chara1to2 = chara2.position - chara1.position
          chara1to2 /= abs(chara1to2)
          movedistance = chara1.radius + chara2.radius - distance
          
          chara1.position -= movedistance * chara1to2
          chara2.position += movedistance * chara1to2

def bullet_and_floor(bullet,floor):
      
     return bullet.position[0] >= floor.origin[0] and bullet.position[0] < floor.origin[0] + floor.xlength and bullet.position[2] >= floor.origin[2] and bullet.position[2] < floor.origin[2] + floor.zlength and (bullet.position[1] + 1.2 - floor.height) * (bullet.before_position[1] + 1.2 - floor.height) <= 0
               
