# Import dependencies
from panda3d.core import ClockObject

from direct.actor.Actor import Actor
from direct.task import Task
import gltf

class Player(Actor):
    def __init__(self):
        # Patch the loader to support GLTF
        #gltf.patch_loader(loader)
        # Load the player model and initialize Actor class
        super().__init__("game/assets/models/ShibaInu.gltf")
        self.setHpr(180, 0, 0)
        # Reparent the model to render
        self.reparentTo(render)
        
        

    '''
    def physics(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        gravity = 5 * dt
        self.speed += gravity
        self.setZ(self, -self.speed)
        if base.physics.touchingGround:
            self.speed = 0
        return Task.cont
    '''
