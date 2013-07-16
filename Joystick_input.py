import time
import pygame

class joyinput:
    def __init__(self,axis=[0,0,-1,0,0,-1],
                 buttons=[0] * 11):
        self.axis = axis
        self.buttons = buttons
        self.js = None

    def getxbox360pad(self):
        for i in range( pygame.joystick.get_count() ):
            js = pygame.joystick.Joystick( i )
            if js.get_name() == 'Microsoft X-Box 360 pad':
                return js
        raise RuntimeError( 'X-Box 360 pad not found' )

    def init(self):
        pygame.init()
        pygame.joystick.init()
        self.js = self.getxbox360pad()
        self.js.init()
    
    def quit(self):
        self.js.quit()
        pygame.quit()
    
    def input(self):
        e = pygame.event.get()
        self.buttons = [0 for i in range(11)]
        for i in e:
            if i.type == pygame.JOYAXISMOTION:
                self.axis[i.axis] = i.value
            elif i.type == pygame.JOYBUTTONDOWN:
                self.buttons[i.button] = 1
            elif i.type == pygame.JOYBUTTONUP:
                self.buttons[i.button] = -1
            elif i.type == pygame.JOYHATMOTION:
                pass
    

def test():
    while True:
        try:
            e = pygame.event.wait()
            print( e )
            print e.type
        except KeyboardInterrupt:
            exit()
if __name__=="__main__":
    #"""
    try:
        pad = joyinput()
        pad.init()
        test()
    finally:
        pad.quit()
        """
    class J:
        def __enter__(self):
            tmp=joyinput()
            tmp.init()
            self.temp=tmp
            return tmp
        def __exit__(self,*):
            self.temp.quit()
            return True
    with J():
        test()#"""
