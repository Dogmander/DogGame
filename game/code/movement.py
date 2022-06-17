from panda3d.core import ClockObject
from direct.task import Task
from .controls import Input
from random import randrange

class Movement:
    def __init__(self):
        self.input = Input()
        self.keyMap = self.input.keyMap
        self.isMoving = self.input.isMoving
    def move(self, task):
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
                base.player.stop()
                base.player.loop("Idle")
                
                self.isMoving = False
         
        
        if base.player.getH() > 360:
            base.player.setH(0)
        if base.player.getH() < 0:
            base.player.setH(360)
        return Task.cont
    