# Import dependencies
from panda3d.core import ClockObject
from direct.task import Task

# Create Physics class
class Physics:
    def __init__(self):
        self.current_speed = 0
        self.dt = ClockObject.getGlobalClock().getDt()
        self.acceleration = 9.81 *  ClockObject.getGlobalClock().getDt()
        self.touching_ground = False
        
    
    def groundState(self, state, entry):
        self.touching_ground = state
        
    def test(self, task):
        
        if not self.touching_ground:
            self.current_speed += self.acceleration 
            base.player.setZ(base.player, -self.current_speed)
        elif self.touching_ground:
            self.current_speed = 0
            base.player.setZ(base.scene.model.getZ())
        return Task.cont
            
    def gravity(self, task):
        self.acceleration = 9.81 * ClockObject.getGlobalClock().getDt()
        if not self.touching_ground:
            self.current_speed += self.acceleration 
            base.player.setZ(base.player, -self.current_speed * self.dt)
            #print(self.current_speed)
        elif self.touching_ground:
            self.current_speed = 0
            base.player.setZ(base.scene.model.getZ())
        if self.current_speed > 10:
            self.current_speed = 10
        if base.player.getZ() < -500:
            base.player.setZ(5)
        return Task.cont
    