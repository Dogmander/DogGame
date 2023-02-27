# Import dependencies
from direct.actor.Actor import Actor
from direct.fsm.FSM import FSM
from panda3d.core import NodePath, CollisionNode, CollisionSphere, CollisionRay
from .constants import *
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
        
        self.playerNP = NodePath('playerNP')
        self.playerNP.reparentTo(base.render)
        
        self.model.reparentTo(self.playerNP)
        self.model.setCollideMask(BitMask32.allOff())
        
        self.playerNP.setPos(0, 0, 15)
        
        self.playerCollider = self.model.attachNewNode(
            CollisionNode('playercnode'))
        
        self.playerCollider.node().addSolid(CollisionSphere(0, -1, 1.2, 1))
        self.playerCollider.node().addSolid(CollisionSphere(0, 1.25, 1.2, 1.25))
        self.playerCollider.show()
        self.playerCollider.node().setFromCollideMask(WALL_MASK)
        self.playerCollider.node().setIntoCollideMask(BitMask32.allOff())
        
        self.raygeometry = CollisionRay(0, 0, 2, 0, 0, -1)
        self.avatarRay = self.playerNP.attachNewNode(
            CollisionNode('avatarRay'))
        self.avatarRay.node().addSolid(self.raygeometry)
        self.avatarRay.node().setFromCollideMask(FLOOR_MASK)
        self.avatarRay.node().setIntoCollideMask(BitMask32.allOff())


        
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
    