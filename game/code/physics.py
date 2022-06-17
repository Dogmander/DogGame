
from panda3d.core import ClockObject
from direct.task import Task

class Physics:
    def __init__(self):
        self.current_speed = 0
        self.dt = ClockObject.getGlobalClock().getDt()
        self.falling_speed = 2 * self.dt 
        self.touchingGround = False
        
    def hitGround(self, entry):
        self.touchingGround = True
        if self.touchingGround:
            self.touchingGround = False
            self.current_speed = 0
        else:
            
            self.current_speed += self.falling_speed
        base.player.setZ(base.scene.model.getZ())
        
        print(self.current_speed)
        
    
            
    def gravity(self, task):
        if self.touchingGround:
            self.current_speed = 0
        elif not self.touchingGround:
            self.current_speed += self.falling_speed
            base.player.setZ(base.player, -self.current_speed)
        print(self.current_speed, self.touchingGround, base.player.getZ())
        return Task.cont
    
