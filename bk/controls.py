from direct.task import Task
from panda3d.core import ClockObject

class Mover:
    def __init__(self):
        self.isMoving = False
        base.accept("h", self.hello)
    def rotation(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        
        if base.keyMap["left"]:
            base.player.setH(base.player.getH() + dt * 60)
        if base.keyMap["right"]:
            base.player.setH(base.player.getH() - dt * 60)
        if base.keyMap["forward"]:
            base.player.setY(base.player, - dt * 30)
        if base.keyMap["backward"]:
            base.player.setY(base.player, + dt * 15)
        
        if base.keyMap["forward"]:
            if not self.isMoving:
                base.player.loop("Gallop")
                self.isMoving = True
        elif base.keyMap["left"] or base.keyMap["right"] or base.keyMap["backward"]:
            if not self.isMoving:
                base.player.loop("Walk")
                self.isMoving = True
        else:
            if self.isMoving:
                base.player.loop("Idle")
                self.isMoving = False
    def hello(self):
        print("Hello")        
        
            
        
        
            
        
        
        if base.player.getH() > 360:
            base.player.setH(0)
        if base.player.getH() < 0:
            base.player.setH(360)
                    
        return Task.cont
    