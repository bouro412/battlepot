from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import gameinput
import gameoutput
ws_states=0
ad_states=0

def display():
    global ws_states,ad_states
    gameoutput.draw(ws_states,ad_states)

def keyboard(key, x, y):
    global ws_states,ad_states
    ws_states,ad_states = gameinput.keyb(key, x, y,ws_states,ad_states)

def keyboardup(key,x,y):
    global ws_states,ad_states
    ws_states,ad_states = gameinput.keyup(key,x,y,ws_states,ad_states)

def real_reshape(w,h):
    gameoutput.reshape(w,h)

def timer(t):
    glutPostRedisplay()
    glutTimerFunc(17,timer,t)

def main():
    glutInit()

    glutInitWindowSize(640,480)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
    glClearColor(0.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0)
    glutCreateWindow("BattlePot")
    
    glutDisplayFunc(display)
    glutReshapeFunc(real_reshape)
    #glutMouseFunc(mouse)
    #glutMotionFunc(dragmotion)
    #glutPassiveMotionFunc(passivemotion)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboardup)
    glutTimerFunc(0,timer,17)

    glutMainLoop()

main()

