from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import gameinput
import gameoutput
import Character

class funcs:
    def __init__(self,p1,ws,ad):
        self.p1 = p1
        self.ws = ws
        self.ad = ad
            
    def display(self):
        gameoutput.draw(self.p1,self.ws,self.ad)

    def keyboard(self,key, x, y):
        self.ws,self.ad = gameinput.keyb(key, x, y,self.ws,self.ad)

    def keyboardup(self,key,x,y):
        self.ws,self.ad = gameinput.keyup(key,x,y,self.ws,self.ad)
        
    def reshape(self,w,h):
        gameoutput.reshape(w,h)
        
    def timer(self,t):
        glutPostRedisplay()
        glutTimerFunc(17,self.timer,t)
        
    def passivemotion(self,x,y):
        print "passive ",x,y

def inits():
    glutInit()
    
    #glutInitWindowSize(640,480)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
    glClearColor(0.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0)
    
    glutGameModeString("1280x800:32@100")
    glutEnterGameMode()
    glutSetCursor(GLUT_CURSOR_NONE)

    #glutCreateWindow("BattlePot")

def register_funcs():
    p1 = Character.player(gameoutput.drawplayer,
                          [0,0,0],[0,0],0)    
    f = funcs(p1,0,0) 
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

