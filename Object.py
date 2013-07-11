from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import Color
import Character

def plane(four_vertex3f,normal,color):
    v = four_vertex3f
    color()
    glBegin(GL_QUADS)
    glVertex3fv(v[0])
    glVertex3fv(v[1])
    glVertex3fv(v[2])
    glVertex3fv(v[3])
    glEnd()
