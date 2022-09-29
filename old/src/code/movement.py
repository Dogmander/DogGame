# Import depenedencies
from panda3d.core import ClockObject

from direct.task import Task
from direct.showbase.PythonUtil import reduceAngle

from .controls import Input
from .player import PlayerFSM

'''
class Movement:
    def __init__(self):
        self.input = Input()
        self.keyMap = self.input.keyMap
        self.isMoving = False
        SPEED_TURN = 60
        SPEED_FW = 30
        SPEED_BW = SPEED_FW / 2
        base.taskMgr.add(self.move, "movement_task")

    def move(self, task):
        dt = ClockObject.getGlobalClock().getDt()

        if self.keyMap["left"]:
            base.player.setH(reduceAngle(base.player.getH() + dt * SPEED_TURN))
        if self.keyMap["right"]:
            base.player.setH(reduceAngle(base.player.getH() - dt * SPEED_TURN))
        if self.keyMap["forward"]:
            base.player.setY(base.player, - dt * SPEED_FW)
        if self.keyMap["backward"]:
            base.player.setY(base.player, + dt * SPEED_BW)

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
        if self.keyMap["jump"]:
            if not self.isMoving:
                base.player.stop()
                base.player.play("Jump_ToIdle")
                self.isMoving = True
            elif self.isMoving:
                base.player.play("Gallop")

        return Task.cont
'''

class Movement:
    def __init__(self):
        self.input = Input()
        self.fsm = PlayerFSM('PlayerFSM')
        self.keyMap = self.input.keyMap
        self.isMoving = False
        
        base.taskMgr.add(self.move, "movement_task")
    
    def move(self, task):
        dt = ClockObject.getGlobalClock().getDt()

        if self.keyMap["left"]:
            base.playerNP.setH(reduceAngle(base.playerNP.getH() + dt * base.player.SPEED_TURN))
        if self.keyMap["right"]:
            base.playerNP.setH(reduceAngle(base.playerNP.getH() - dt * base.player.SPEED_TURN))
        if self.keyMap["forward"]:
            base.playerNP.setY(base.playerNP, + dt * base.player.SPEED_FW)
            
        if self.keyMap["backward"]:
            base.playerNP.setY(base.playerNP, - dt * base.player.SPEED_BW)
    
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
        if self.keyMap["jump"]:
            if not self.isMoving:
                base.player.stop()
                base.player.play("Jump_ToIdle")
                self.isMoving = True
            elif self.isMoving:
                base.player.play("Gallop")

        return Task.cont
    
   