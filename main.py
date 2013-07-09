from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import gameinput
import gameoutput
import Character

class mainit:
    def __init__(self,p1,ws,ad):
        self.p1 = p1
        self.ws = ws
        self.ad = ad
            
    def real_display(self):
        gameoutput.draw(self.p1,self.ws,self.ad)

    def keyboard(self,key, x, y):
        self.ws,self.ad = gameinput.keyb(key, x, y,self.ws,self.ad)

    def keyboardup(self,key,x,y):
        self.ws,self.ad = gameinput.keyup(key,x,y,self.ws,self.ad)
        
    def real_reshape(self,w,h):
        gameoutput.reshape(w,h)
        
    def timer(self,t):
        glutPostRedisplay()
        glutTimerFunc(17,self.timer,t)

def main():
    glutInit()
    
    p1 = Character.player(gameoutput.drawplayer,
                          [0,0,0],[0,0],0)
    m = mainit(p1,0,0)
    glutInitWindowSize(640,480)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
    glClearColor(0.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0)
    glutCreateWindow("BattlePot")
    
    glutDisplayFunc(m.real_display)
    glutReshapeFunc(m.real_reshape)
    #glutMouseFunc(mouse)
    #glutMotionFunc(dragmotion)
    #glutPassiveMotionFunc(passivemotion)
    glutKeyboardFunc(m.keyboard)
    glutKeyboardUpFunc(m.keyboardup)
    glutTimerFunc(0,m.timer,17)

    glutMainLoop()

main()

