from direct.showbase.DirectObject import DirectObject
from direct.task import Task
from panda3d.core import ClockObject

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

    def rotation(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        
        if self.keyMap["left"]:
            base.player.setH(base.player.getH() + dt * 60)
        if self.keyMap["right"]:
            base.player.setH(base.player.getH() - dt * 60)
        if self.keyMap["forward"]:
            base.player.setY(base.player, - dt * 30)
        if self.keyMap["backward"]:
            base.player.setY(base.player, + dt * 15)
        
        if self.keyMap["forward"]:
            if not self.isMoving:
                base.player.loop("Gallop")
                self.isMoving = True
        elif self.keyMap["left"] or self.keyMap["right"] or self.keyMap["backward"]:
            if not self.isMoving:
                base.player.loop("Walk")
                self.isMoving = True
        else:
            if self.isMoving:
                base.player.loop("Idle")
                self.isMoving = False
         
        
        if base.player.getH() > 360:
            base.player.setH(0)
        if base.player.getH() < 0:
            base.player.setH(360)
        
        return Task.cont
    