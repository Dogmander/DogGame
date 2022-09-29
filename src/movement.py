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
        self.input.keyMap = self.input.input.keyMap
        self.isMoving = False
        SPEED_TURN = 60
        SPEED_FW = 30
        SPEED_BW = SPEED_FW / 2
        base.taskMgr.add(self.move, "movement_task")

    def move(self, task):
        dt = ClockObject.getGlobalClock().getDt()

        if self.input.keyMap["left"]:
            base.player.setH(reduceAngle(base.player.getH() + dt * SPEED_TURN))
        if self.input.keyMap["right"]:
            base.player.setH(reduceAngle(base.player.getH() - dt * SPEED_TURN))
        if self.input.keyMap["forward"]:
            base.player.setY(base.player, - dt * SPEED_FW)
        if self.input.keyMap["backward"]:
            base.player.setY(base.player, + dt * SPEED_BW)

        if self.input.keyMap["forward"]:
            if not self.isMoving:
                base.player.loop("Gallop")
                self.isMoving = True
        if self.input.keyMap["left"] or self.input.keyMap["right"] or self.input.keyMap["backward"]:
            if not self.isMoving:
                base.player.loop("Walk")
                self.isMoving = True
        else:
            if self.isMoving:
                base.player.stop()
                base.player.loop("Idle")
                self.isMoving = False
        if self.input.keyMap["jump"]:
            if not self.isMoving:
                base.player.stop()
                base.player.play("Jump_ToIdle")
                self.isMoving = True
            if self.isMoving:
                base.player.play("Gallop")

        return Task.cont
'''

class Movement:
    def __init__(self):
        self.input = Input()
        self.fsm = PlayerFSM('PlayerFSM')
        
        base.taskMgr.add(self.move, "movement_task")
    
    def move(self, task):
        dt = globalClock.getDt()
        moving = False
        if self.input.keyMap["left"]:
            base.playerNP.setH(reduceAngle(base.playerNP.getH() + dt * base.player.SPEED_TURN))
            moving = True
            
        if self.input.keyMap["right"]:
            base.playerNP.setH(reduceAngle(base.playerNP.getH() - dt * base.player.SPEED_TURN))
            moving = True
            
        if self.input.keyMap["forward"]:
            base.playerNP.setY(base.playerNP, + dt * base.player.SPEED_FW)
            moving = True
            
        if self.input.keyMap["backward"]:
            base.playerNP.setY(base.playerNP, - dt * base.player.SPEED_BW)
            moving = True
            
        if moving and self.fsm.state != 'Walk':
            self.fsm.request('Walk')
        elif not moving and self.fsm.state != 'Idle':
            self.fsm.request('Idle')
    
        '''
        if self.input.keyMap["forward"]:
            if not self.isMoving:
                base.player.loop("Gallop")
                self.isMoving = True
        if self.input.keyMap["left"] or self.input.keyMap["right"] or self.input.keyMap["backward"]:
            if not self.isMoving:
                base.player.loop("Walk")
                self.isMoving = True
        else:
            if self.isMoving:
                base.player.stop()
                base.player.loop("Idle")
                self.isMoving = False
        if self.input.keyMap["jump"]:
            if not self.isMoving:
                base.player.stop()
                base.player.play("Jump_ToIdle")
                self.isMoving = True
            if self.isMoving:
                base.player.play("Gallop")
        '''
        
        return Task.cont
    
   