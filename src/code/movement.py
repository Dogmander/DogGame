# Import depenedencies
from panda3d.core import ClockObject
from direct.task import Task
from .controls import Input
from direct.showbase.PythonUtil import reduceAngle


class Movement:
    def __init__(self):
        self.input = Input()
        self.keyMap = self.input.keyMap
        self.isMoving = False
        self.speed_turning = 60
        self.speed_forward = 30
        self.speed_backward = self.speed_forward / 2
        base.taskMgr.add(self.move, "movement_task")

    def move(self, task):
        dt = ClockObject.getGlobalClock().getDt()

        if self.keyMap["left"]:
            base.player.setH(reduceAngle(base.player.getH() + dt * self.speed_turning))
        if self.keyMap["right"]:
            base.player.setH(reduceAngle(base.player.getH() - dt * self.speed_turning))
        if self.keyMap["forward"]:
            base.player.setY(base.player, - dt * self.speed_forward)
        if self.keyMap["backward"]:
            base.player.setY(base.player, + dt * self.speed_backward)

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
