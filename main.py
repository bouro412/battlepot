from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import gameinput
import gameoutput
import Character
import playerpot
import Joystick_input
import enemypot

class funcs:
    def __init__(self,joy,objects):
        self.objects = objects
        self.joy = joy
        
            
    def display(self):
         gameoutput.draw(self.objects,self.joy)

    def keyboard(self,key, x, y):
        gameinput.keyb(key, x, y,self.joy)

    def keyboardup(self,key,x,y):
        gameinput.keyup(key,x,y)
        
    def reshape(self,w,h):
        gameoutput.reshape(w,h)
        
    def timer(self,t):
        glutPostRedisplay()
        glutTimerFunc(17,self.timer,t)
        
    def passivemotion(self,x,y):
        print "passive ",x,y

def inits():
    glutInit()
    
    glutInitWindowSize(640,480)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
    glClearColor(0.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0)
    
    """glutGameModeString("1280x800:32@100")
    glutEnterGameMode()
    glutSetCursor(GLUT_CURSOR_NONE)"""

    glutCreateWindow("BattlePot")

def register_funcs():
    p1 = playerpot.normalpot(0, [0,0,0],[0,0],0)
    e1 = enemypot.normalpot(1,[5,0,5],[0,0],0)
    e2 = Character.testsphere(0,[0,0,0],[0,0],0)
    joy = Joystick_input.joyinput()
    joy.init()
    objects = [p1,e2]
    f = funcs(joy,objects) 
    glutDisplayFunc(f.display)
    glutReshapeFunc(f.reshape)
    #glutMouseFunc(mouse)
    #glutMotionFunc(dragmotion)
    #glutPassiveMotionFunc(f.passivemotion)
    glutKeyboardFunc(f.keyboard)
    glutKeyboardUpFunc(f.keyboardup)
    glutTimerFunc(0,f.timer,17)

def main():
    inits()
    register_funcs()

    glutMainLoop()


main()

