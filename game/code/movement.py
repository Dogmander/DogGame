# Import depenedencies
from panda3d.core import ClockObject
from direct.task import Task
from .controls import Input
from direct.showbase.PythonUtil import reduceAngle
class Movement:
    def __init__(self):
        
        self.input = Input()
        self.keyMap = self.input.keyMap
        self.isMoving = self.input.isMoving
        
    def move(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        
        if self.keyMap["left"]:
            base.player.setH(reduceAngle(base.player.getH() + dt * 60))
        if self.keyMap["right"]:
            base.player.setH(reduceAngle(base.player.getH() - dt * 60))
        if self.keyMap["forward"]:
            base.player.setY(base.player, - dt * 30)
        if self.keyMap["backward"]:
            base.player.setY(base.player, + dt * 15)
        if self.keyMap["jump"]:
            if base.physics.touching_ground:
                base.physics.touching_ground = False
                base.physics.current_speed = 2.5
            if not base.physics.touching_ground:
                base.physics.current_speed += base.physics.acceleration
                base.player.setZ(base.player, base.physics.current_speed)
           
        
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
         
        
        print(base.physics.touching_ground)
        print(base.physics.current_speed)
        print(base.physics.acceleration)
        return Task.cont
    
        
        
        