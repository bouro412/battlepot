from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def red():
    red = (1.0,0.0,0.0,1.0)
    shin = 51.2
    colors(red,red,red,shin)

def green():
    green = (0.0,1.0,0.0,1.0)
    shin = 51.2
    colors(green,green,green,shin)

def gold():
    amb = (0.247250, 0.1995, 0.07450, 1.0)
    diff = (0.75164, 0.60648, 0.22648, 1.0)
    spe = (0.628281, 0.555802, 0.366065, 1.0)
    shin = 51.2
    
    colors(amb,diff,spe,shin)

def colors(amb,diff,spe,shin):
    glColor4fv(amb)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT)
    glColor4fv(diff)
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    glColor4fv(spe)
    glColorMaterial(GL_FRONT_AND_BACK, GL_SPECULAR)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shin)
