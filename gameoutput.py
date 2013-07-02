from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
x=0.0
y=0.0
angle=0.0
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
               0,1,0)

def draw(ws_states,ad_states):
     glClearColor(0,1,1,1)
     glClearDepth(1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glEnable(GL_DEPTH_TEST)

     camera(ws_states, ad_states)
     light()

     drawxyz()
     drawplayer()
     #drawearth()
        
     glDisable(GL_DEPTH_TEST)
     glutSwapBuffers()
    
def drawxyz():
     white = [1,1,1,1]
     glPushMatrix()
     glBegin(GL_LINES)
     glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT, white)
     glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE, white)
     glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR, white)
     glVertex3f(0,0,0)
     glVertex3f(100,0,0)
     glVertex3f(0,0,0)
     glVertex3f(0,100,0)
     glVertex3f(0,0,0)
     glVertex3f(0,0,100)
     glEnd()
     glPopMatrix()

def drawearth():
     red = [1,0,0,1]
     green = [0,1,0,1]
     glPushMatrix()
     glBegin(GL_QUADS)
     for i in range(100):
          for j in range(100):
               glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT, red)
               glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE, red)
               glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR, red)
               glVertex3f(i,0,j)
               glVertex3f(i+0.5,0,j)
               glVertex3f(i+0.5,0,j+0.5)
               glVertex3f(i,0,j+0.5)
               glVertex3f(i,0,j)
               glVertex3f(i-0.5,0,j)
               glVertex3f(i-0.5,0,j-0.5)
               glVertex3f(i,0,j-0.5)
               glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT,green)
               glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE,green)
               glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,green)
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
     global x,y,angle
     glPushMatrix()

     glTranslatef(x,0.7,y)
     glRotatef(angle,0,1,0)
     golden_pot()
 
     glPopMatrix()

def golden_pot():
     gold_amb = [0.247250, 0.1995, 0.07450, 1.0]
     gold_diff = [0.75164, 0.60648, 0.22648, 1.0]
     gold_spe = [0.628281, 0.555802, 0.366065, 1.0]
     gold_shin = 51.2
     
     glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, gold_amb)    
     glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, gold_diff)
     glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, gold_spe)
     glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, gold_shin)

     glutSolidTeapot(1.0)
