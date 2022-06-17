from direct.showbase.DirectObject import DirectObject



class Input(DirectObject):
    def __init__(self):
        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "backward": 0}
        
        self.isMoving = False
        self.accept("w", self.setKey, ["forward", True])
        self.accept("s", self.setKey, ["backward", True])
        self.accept("a", self.setKey, ["left", True])
        self.accept("d", self.setKey, ["right", True])
        self.accept("w-up", self.setKey, ["forward", False])
        self.accept("s-up", self.setKey, ["backward", False])
        self.accept("a-up", self.setKey, ["left", False])
        self.accept("d-up", self.setKey, ["right", False])
        self.accept("w", self.setKey, ['forward', True])
        self.accept("h", self.setKey, ['left', True])
        
        
    def setKey(self, key, value):
        self.keyMap[key] = value
        print(self, key, value)

    
        
    