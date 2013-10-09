from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class title:
    startup = False
    selection = 0
    select_recovery = 0
    
    def move(joyinput):
        A_button = joyinput.buttons[0]
        L_Stick = joyinput.axis[1]
        B_button = joyinput.buttons
        if self.select_recovery > 0:
            self.select_recovery -= 17
        if not startup:
            if A_button == 1:
                self.startup = True
        else:
            if abs(L_Stick) > 0.7 and self.select_recovery <= 0:
                self.selection -= L_Stick / abs(L_Stick)
                self.select_recovery = 500
            if A_button == 1:
                self.ChangeScene(self.selection)
            

    def draw():
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, 640, 0, 480)
        #MODELVIEW行列を操作
        glMatrixMode(GL_MODELVIEW) 
        glPushMatrix() #MODELVIEW行列を保存
        glLoadIdentity()
        #いろいろ無効にする
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)

        glBegin()
