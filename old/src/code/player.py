# Import dependencies
from direct.actor.Actor import Actor
from direct.fsm.FSM import FSM


class Player(Actor):
    SPEED_TURN = 60
    SPEED_FW = 30
    SPEED_BW = SPEED_TURN / 2

    def __init__(self):
        # TODO: instead of inheritting actor, init actor within class (this is better for reasons)
        
        # Load the player model and initialize Actor class
        super().__init__("src/assets/models/shibacolor.gltf")
        self.setHpr(180, 0, 0)
        # Reparent the model to render
        self.reparentTo(render)
        self.set_pos(base.scene.spawn_point.get_pos())


class PlayerFSM(FSM):

    def enterWalk(self):
        base.player.loop('Walk')
        print("Entered walk state")

    def exitWalk(self):
        base.player.stop()
        print("Walk state exited")
