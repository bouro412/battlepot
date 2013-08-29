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
    amb = (0.247250, 0.1995, 0.07450, 0.0)
    diff = (0.75164, 0.60648, 0.22648, 0.0)
    spe = (0.628281, 0.555802, 0.366065, 0.0)
    shin = 51.2
    
    colors(amb,diff,spe,shin)

def ruby():
    amb = (0.1745,   0.01175,  0.01175,   1.0)
    diss = (0.61424,  0.04136,  0.04136,   1.0)
    spe = (0.727811, 0.626959, 0.626959,  1.0)
    shin = 76.8

    colors(amb,diss,spe,shin)

def yellow_rubber():
    colors((0.05,  0.05,    0.0,  1.0),
           (0.5,   0.5,     0.4,  1.0),
           (0.7,   0.7,     0.04, 1.0),
           50.0)

def yellow_plastic():
    colors( (0.0,  0.0,0.0,  1.0),
            (0.5,  0.5, 0.0,  1.0),
            (0.60, 0.60, 0.50, 1.0),
            32
            )
def brass():
    colors((0.329412,  0.223529, 0.027451, 1.0),
           (0.780392,  0.568627, 0.113725, 1.0),
           (0.992157,  0.941176, 0.807843, 1.0),
           27.89743616)

def chrome():
    colors((0.25,    0.25,     0.25,     1.0),
           (0.4,     0.4,      0.4,      1.0),
           (0.774597,0.774597, 0.774597, 1.0),
           76.8
           )

def turquoise():
    colors((0.1,     0.18725, 0.1745,  1.0),
           (0.396,   0.74151, 0.69102, 1.0),
           (0.297254,0.30829, 0.306678,1.0),
           12.8)

def colors(amb,diff,spe,shin):
    glColor4fv(amb)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT)
    glColor4fv(diff)
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    glColor4fv(spe)
    glColorMaterial(GL_FRONT_AND_BACK, GL_SPECULAR)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shin)
