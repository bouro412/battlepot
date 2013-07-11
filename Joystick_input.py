import time
import pygame

def getxbox360pad():
    for i in range( pygame.joystick.get_count() ):
        js = pygame.joystick.Joystick( i )
        if js.get_name() == 'Microsoft X-Box 360 pad':
            return js
    raise RuntimeError( 'X-Box 360 pad not found' )

def init():
    global js
    pygame.init()
    pygame.joystick.init()
    js = getxbox360pad()
    js.init()

def quit():
    js.quit()
    pygame.quit()

def test():
    while True:
        try:
            e = pygame.event.wait()
            print e.type()
            if e.value >= 0.7:
                print( e )
        except KeyboardInterrupt:
            system.exit(1)
if __name__=="__main__":
    try:
        init()
        test()
    finally:
        quit()

