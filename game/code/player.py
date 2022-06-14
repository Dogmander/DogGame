# Import dependencies
from direct.actor.Actor import Actor
import gltf

class Player(Actor):
    def __init__(self):
        # Patch the loader to support GLTF
        gltf.patch_loader(loader)
        # Load the player model and initialize Actor class
        super().__init__("game/assets/models/ShibaInu.gltf")
        # Reparent the model to render
        self.reparentTo(render)
