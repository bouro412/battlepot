from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import Color
import Character
import Object
import util
#bullets = []
hitcount = 0
     
def draw(objects,joy):
     global hitcount
     glClearColor(0,1,1,1)
     glClearDepth(1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glEnable(GL_DEPTH_TEST)
     glEnable(GL_COLOR_MATERIAL)
     
     light()  
     
     joy.input()

     for i,ob in enumerate(objects):
          if isinstance(ob, Character.player):
               ob.camera()
               objects.extend(ob.input(joy))
               ob.draw()
          elif isinstance(ob, Character.enemy):
               ob.draw()
          elif isinstance(ob,Character.character):
               ob.draw()
          elif isinstance(ob, Object.Bullet):
               ob.draw()
               if ob.fadeout():
                    del objects[i]
     for i in range(len(objects)-1):
          for j in range(i+1,len(objects)):
               if isinstance(objects[i],Character.character):
                    if objects[i].collision_detection(objects[j]):
                         print "HIT!!",hitcount
                         hitcount += 1
                         print "j",objects[j].position,util.norm(util.Vec(objects[j].position))
                         del objects[j]
               elif isinstance(objects[j],Character.character):
                    if objects[j].collision_detection(objects[i]):
                         print "HIT!!",hitcount
                         hitcount += 1
                         print "i",objects[i].position
                         del objects[i]
          
     glDisable(GL_COLOR_MATERIAL)
     glDisable(GL_DEPTH_TEST)
     glutSwapBuffers()

def reshape(w,h):
     glViewport(0,0,w,h)
    
     glMatrixMode(GL_PROJECTION)
     glLoadIdentity()
     gluPerspective(45,float(w)/h,1.0,1000)
    
     glMatrixMode(GL_MODELVIEW)


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

def drawplayer():
     Color.gold()
     glutSolidTeapot(1)




