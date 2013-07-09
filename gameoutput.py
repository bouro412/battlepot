from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import Color
import Character
#x=0.0
#y=0.0
#angle=0.0
"""
def camera(ws_states, ad_states):
     global x,y,angle
     if ws_states != 0:
          x += cos(radians(angle)) * ws_states * 0.5
          y += -sin(radians(angle)) * ws_states * 0.5
     if ad_states != 0:
          angle += ad_states * 3     
     glLoadIdentity()
     camera_position = [x -10 * cos(radians(angle))
                        ,2,y + 10 * sin(radians(angle))]
     camera_vector = [x - camera_position[0],0,y - camera_position[2]]
     gluLookAt(camera_position[0],camera_position[1],camera_position[2],
               camera_position[0] + camera_vector[0] * 10,1,
               camera_position[2] + camera_vector[2] * 10,
               0,1,0)"""
     
def draw(p1,ws_states,ad_states):
     glClearColor(0,1,1,1)
     glClearDepth(1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glEnable(GL_DEPTH_TEST)
     glEnable(GL_COLOR_MATERIAL)
     
     light()  
     
     p1.camera()
     p1.input(ws_states,ad_states)
     p1.draw()
     
     glPushMatrix()
     Color.red()
     glTranslatef(10,0.7,10)
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




