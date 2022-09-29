# Import dependencies
from direct.actor.Actor import Actor
from direct.fsm.FSM import FSM


class Player():
    SPEED_TURN = 60
    SPEED_FW = 30
    SPEED_BW = SPEED_TURN / 2

    def __init__(self):
        # TODO: instead of inheritting actor, init actor within class (this is better for reasons)
        
        # Load the player model and initialize Actor class
        self.model = Actor('assets/gltf/shibacolor.gltf')
        self.model.set_h(180)
        # Reparent the model to render
        self.model.reparentTo(render)
        
class PlayerFSM(FSM):
    
    def enterIdle(self):
        base.player.model.loop('Idle')
    
    def exitIdle(self):
        base.player.model.stop()
    
    def enterWalk(self):
        base.player.model.loop('Walk')
        print("Entered walk state")

    def exitWalk(self):
        base.player.model.stop()
        print("Walk state exited")
    