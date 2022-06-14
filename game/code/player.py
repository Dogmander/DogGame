# Import dependencies
from direct.actor.Actor import Actor
import gltf

class Player(Actor):
    def __init__(self):
        # Patch the loader to support GLTF
        gltf.patch_loader(loader)
        # Load the player model and initialize Actor class
        super().__init__("game/assets/models/ShibaInu.gltf")
        self.setHpr(180, 0, 0)
        # Reparent the model to render
        self.reparentTo(render)
        
        
