import Keyboardconfig

class Input:
    def __init__(self):
        self.move = [0, 0]
        self.camera = [0, 0]
        self.cameralock = 0
        self.shot = 0
        self.jump = 0
        self.dash = 0

    def eventhandler(self, event):
        raise NotImplementedError

    def flamehandler(self):
        raise NotImplementedError

class KeyboardInput(Input):
    def eventhadler(self, event):
        Keyconfig.eventhandler()
