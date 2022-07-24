# Import dependencies
from direct.showbase.DirectObject import DirectObject
'''
class Input(DirectObject):
    def __init__(self):
        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "backward": 0, "jump": 0}
    
        self.isMoving = False
        base.accept("w", self.setKey, ["forward", True])
        base.accept("s", self.setKey, ["backward", True])
        base.accept("a", self.setKey, ["left", True])
        base.accept("d", self.setKey, ["right", True])
        #base.accept("space", self.setKey, ["jump", True])
        base.accept("w-up", self.setKey, ["forward", False])
        base.accept("s-up", self.setKey, ["backward", False])
        base.accept("a-up", self.setKey, ["left", False])
        base.accept("d-up", self.setKey, ["right", False])
        #base.accept("space-up", self.setKey, ['jump', False])
        #base.accept("space", base.physics)
    
    def setKey(self, key, value):
        self.keyMap[key] = value
        print(self, key, value)
'''


class Input(DirectObject):
    def __init__(self):
        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "backward": 0, "jump": 0}

        self.accept("w", self.setKey, ["forward", True])
        self.accept("s", self.setKey, ["backward", True])
        self.accept("a", self.setKey, ["left", True])
        self.accept("d", self.setKey, ["right", True])
        #base.accept("space", self.setKey, ["jump", True])
        self.accept("w-up", self.setKey, ["forward", False])
        self.accept("s-up", self.setKey, ["backward", False])
        self.accept("a-up", self.setKey, ["left", False])
        self.accept("d-up", self.setKey, ["right", False])
        #base.accept("space-up", self.setKey, ['jump', False])
        #base.accept("space", base.physics)
        self.accept("space", base.physics.jump)
        #self.accept('b', base.player.bark)
        

    def setKey(self, key, value):
        self.keyMap[key] = value
        print(self, key, value)
