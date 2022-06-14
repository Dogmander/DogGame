from direct.task import Task
from panda3d.core import ClockObject

class Mover:
    def __init__(self):
        self.isMoving = False
        
    def rotation(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        
        if base.keyMap["left"]:
            base.player.setH(base.player.getH() + dt * 60)
        if base.keyMap["right"]:
            base.player.setH(base.player.getH() - dt * 60)
        if base.keyMap["forward"]:
            base.player.setY(base.player.getY() + dt * 75)
        if base.keyMap["backward"]:
            base.player.setY(base.player.getY() - dt * 60)
            base.player.setY
            
        if base.keyMap["forward"] or base.keyMap["left"] or base.keyMap["right"] or base.keyMap["backward"]:
            if self.isMoving is False:
                base.player.loop("Walk")
                self.isMoving = True
            else:
                if self.isMoving:
                    base.player.stop()
                    self.isMoving = False
                    
        if base.keyMap["backward"]:
            base.player.setPlayRate(-1, "Walk")
        else:
            base.player.setPlayRate(1, "Walk")
        
        if base.player.getH() > 360:
            base.player.setH(0)
        if base.player.getH() < 0:
            base.player.setH(360)
        print(self.isMoving)
        return Task.cont
    