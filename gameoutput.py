# -*- coding: utf-8 -*-

"""
メインルーチンはこの中のdraw関数で定義されている。
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import color
import character
import bullet
import util
#bullets = []
hitcount = 0
     
def draw(objects,joy):
     global hitcount
     #描画設定の初期化
     glClearColor(0,1,1,1)
     glClearDepth(1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glEnable(GL_DEPTH_TEST)
     glEnable(GL_COLOR_MATERIAL)
     
     light()  
     #ジョイスティックの読み取り
     joy.input()
     #オブジェクトの移動と描画
     # objects = [x for x in objects if x.isalive()]
     for i, obj in reversed( tuple( enumerate( objects ) ) ):
          if not obj.isalive():
               del objects[ i ]
     for ob in objects[:]:
          ob.move(joy,objects)
          
     #衝突判定
     for i in range(len(objects)-1):
          for j in range(i+1,len(objects)):
               if isinstance(objects[i],character.character):
                    if objects[i].collision_detection(objects[j]):
                         print "HIT!!",hitcount
                         hitcount += 1
                         objects[j].kill()
               elif isinstance(objects[j],character.character):
                    if objects[j].collision_detection(objects[i]):
                         print "HIT!!",hitcount
                         hitcount += 1
                         objects[i].kill()

     for ob in objects:
          ob.draw()
          
     #描画の後処理
     glDisable(GL_COLOR_MATERIAL)
     glDisable(GL_DEPTH_TEST)
     glutSwapBuffers()

#最初に一度だけ呼ばれる。カメラの初期化を行っている。いじる必要はない。
def reshape(w,h):
     glViewport(0,0,w,h)
    
     glMatrixMode(GL_PROJECTION)
     glLoadIdentity()
     gluPerspective(45,float(w)/h,1.0,1000)
    
     glMatrixMode(GL_MODELVIEW)

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





