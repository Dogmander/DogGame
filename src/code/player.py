# Import dependencies
from direct.actor.Actor import Actor


class Player(Actor):
    def __init__(self):

        # Load the player model and initialize Actor class
        super().__init__("src/assets/models/shibacolor.gltf")
        self.setHpr(180, 0, 0)
        # Reparent the model to render
        self.reparentTo(render)
