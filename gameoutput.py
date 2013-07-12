from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import Color
import Character
     
def draw(p1,joy):
     glClearColor(0,1,1,1)
     glClearDepth(1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glEnable(GL_DEPTH_TEST)
     glEnable(GL_COLOR_MATERIAL)
     
     light()  
     
     joy.input()
     p1.camera()
     p1.input(joy)
     p1.draw()
     
     glPushMatrix()
     Color.red()
     glTranslatef(10,0.7,0)
     glutSolidTeapot(1)
     glPopMatrix()
     
     glDisable(GL_COLOR_MATERIAL)
     glDisable(GL_DEPTH_TEST)
     glutSwapBuffers()
    
def drawxyz():
     
     glPushMatrix()
     glBegin(GL_LINES)
     glColor(0,0,0,1)
     glVertex3f(0,0,0)
     glVertex3f(100,0,0)
     glVertex3f(0,0,0)
     glVertex3f(0,100,0)
     glVertex3f(0,0,0)
     glVertex3f(0,0,100)
     glEnd()
     glPopMatrix()

def drawearth():
     red = (1,0,0,1)
     green = (0,1,0,1)
     glPushMatrix()    
     glBegin(GL_QUADS)
     for i in range(10):
          for j in range(10):
               glColor4fv(red)
               glVertex3f(i,0,j)
               glVertex3f(i+0.5,0,j)
               glVertex3f(i+0.5,0,j+0.5)
               glVertex3f(i,0,j+0.5)
               glVertex3f(i,0,j)
               glVertex3f(i-0.5,0,j)
               glVertex3f(i-0.5,0,j-0.5)
               glVertex3f(i,0,j-0.5)
               glColor4fv(green)
               glVertex3f(i,0,j)
               glVertex3f(i+0.5,0,j)
               glVertex3f(i+0.5,0,j-0.5)
               glVertex3f(i,0,j-0.5)
               glVertex3f(i,0,j)
               glVertex3f(i-0.5,0,j)
               glVertex3f(i-0.5,0,j+0.5)
               glVertex3f(i,0,j+0.5)
     glEnd()
     glPopMatrix()

def reshape(w,h):
     glViewport(0,0,w,h)
    
     glMatrixMode(GL_PROJECTION)
     glLoadIdentity()
     gluPerspective(30,float(w)/h,1.0,100)
    
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




