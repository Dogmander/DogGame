# Import dependencies
from panda3d.core import ClockObject
from direct.task import Task

# Create Physics class
class Physics:
    def __init__(self):
        self.speed_vertical = 0
        self.dt = ClockObject.getGlobalClock().getDt()
        self.acceleration = 9.81 *  ClockObject.getGlobalClock().getDt()
        self.touching_ground = False
        
    
    def groundState(self, state, entry):
        self.touching_ground = state
        
    def test(self, task):
        
        if not self.touching_ground:
            self.speed_vertical += self.acceleration 
            base.player.setZ(base.player, -self.speed_vertical)
        elif self.touching_ground:
            self.speed_vertical = 0
            base.player.setZ(base.scene.model.getZ())
        return Task.cont
            
    def gravity(self, task):
        self.acceleration = 9.81 * ClockObject.getGlobalClock().getDt()
        if not self.touching_ground:
            self.speed_vertical += self.acceleration 
            base.player.setZ(base.player, -self.speed_vertical * self.dt)
            #print(self.speed_vertical)
        elif self.touching_ground:
            self.speed_vertical = 0
            base.player.setZ(base.scene.model.getZ())
        if self.speed_vertical > 10:
            self.speed_vertical = 10
        if base.player.getZ() < -500:
            base.player.setPos(0, 0, 1.5)
            base.physics.speed_vertical = 0
        return Task.cont
    # Todo: implement better jumping
    def jump(self):
        if self.touching_ground:
            self.touching_ground = False
            base.player.play('Jump')
            base.player.setZ(base.playerNP, 10)
            print("Jumped")
        base.player.play('Jump')
        base.player.setZ(base.playerNP, 10)
        print("Jumped")