# -*- coding: utf-8 -*-
"""
このファイルを実行するとゲームが起動する。
このファイルでは初期化をしており、メインのルーチンはgameoutput中のdraw関数で行われている。
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import gameinput
import gameoutput
import character
import joystick_input
import gamemap

#glut側で使われる関数群をまとめたクラス
class funcs:
    def __init__(self,Map,joy,objects):
        self.Map = Map
        self.objects = objects
        self.joy = joy
            
    def display(self):
         gameoutput.step(self.objects,self.joy,self.Map)

    def keyboard(self,key, x, y):
        gameinput.keyb(key, x, y,self.joy)

    def keyboardup(self,key,x,y):
        gameinput.keyup(key,x,y)
        
    def reshape(self,w,h):
        glViewport(0,0,w,h)
    
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(30,float(w)/h,1.0,1000)
    
        glMatrixMode(GL_MODELVIEW)

        
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
    #オブジェクトリストの初期化
    objects = []
    Map = gamemap.Map(0)
    #ジョイスティック入力の初期化
    joy = joystick_input.joyinput()
    joy.init()
    #glutの初期化
    f = funcs(Map,joy,objects) 
    glutDisplayFunc(f.display)
    glutReshapeFunc(f.reshape)
    glutKeyboardFunc(f.keyboard)
    glutKeyboardUpFunc(f.keyboardup)
    glutTimerFunc(0,f.timer,17)

def main():
    inits()
    register_funcs()

    glutMainLoop()

if __name__ == "__main__":
    main()

