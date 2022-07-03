# Import dependencies
from turtle import left
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
from game.code.player import Player
from game.code.level import Level
from game.code.debug import Debug
from game.code.controls import Input
from game.code.movement import Movement
from game.code.physics import Physics
#from panda3d.core import loadPrcFileData
#loadPrcFileData("", "want-directtools #t")
#loadPrcFileData("", "want-tk #t")

# Load settings
loadPrcFile('settings.prc')

class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Disables camera control via mouse (this is required for the camera position to be able to be adjusted in the code)
        #self.disableMouse()
        
        
        self.debug = Debug()
        # Create level
        self.scene = Level()
        
        #self.input = Input()
        self.movement = Movement()
        self.physics = Physics()
        
        
        taskMgr.add(self.movement.move, "movement_task")
        
        # Create players
        self.player = Player()
        self.player.setZ(1)
        self.player2 = Player()
        
        # Move second player to the right so it doesn't clip into first player
        self.player2.setPos(2, 0, 0)
        
        # Animations for testing
        #self.player.loop("Idle")
        self.player2.loop("Gallop")
        
        # Add temporary lights, these will be replaced when I figure out better lighting    
        dlight = DirectionalLight('my dlight')
        dlnp = self.render.attachNewNode(dlight)
        dlight.setColor((1, 1, 1, 1))
        dlnp.setHpr(0, 192, 0)
        self.render.setLight(dlnp)
        
        
        self.cTrav = CollisionTraverser()
        
        
        self.pnodePath = self.scene.model.attachNewNode(CollisionNode('pnode'))
        self.pnodePath.node().addSolid(CollisionPolygon(Point3(-10, -10, 0), Point3(10, -10, 0),
                                                        Point3(10, 10, 0), Point3(-10, 10, 0)))
        
        print(self.scene.model.getTightBounds())
        self.pnodePath.show()
       
        self.playerCol = CollisionNode('playerCol')
        #self.playerCol.addSolid(CollisionSphere(0, 0, 1, 0.5))
        self.playerCol.addSolid(CollisionSphere(0, -1, 1.2, 1.25))
        self.playerCol.addSolid(CollisionSphere(0, 0.5, 1.2, 1.25))
        self.playerCol.setFromCollideMask(CollideMask.bit(0))
        self.playerCol.setIntoCollideMask(CollideMask.allOff())
        self.playerColNp = self.player.attachNewNode(self.playerCol)
        self.playerPusher = CollisionHandlerPusher()
        self.playerPusher.horizontal = True
        
        self.playerPusher.addCollider(self.playerColNp, self.player)
        self.cTrav.addCollider(self.playerColNp, self.playerPusher)
        self.playerColNp.show()
        self.cTrav.showCollisions(render)
        print(self.cTrav.getColliders())
        
        taskMgr.add(base.physics.gravity, "gravity_task")
        #taskMgr.add(self.physics.test, "test")
        self.playerPusher.addInPattern('player-in-pnode')
        self.playerPusher.addOutPattern('player-out-pnode')
        self.playerPusher.addAgainPattern('player-again-pnode')
        
        #self.accept('player-into-pnode', self.hitGround)
        self.accept('player-in-pnode', self.physics.groundState, [True])
        self.accept('player-out-pnode', self.physics.groundState, [False])
        self.accept('player-again-pnode', self.physics.groundState, [True])

        '''
        self.fromObject = self.player.attachNewNode(CollisionNode('colNode'))
        self.fromObject.node().addSolid(CollisionRay(0, 0, 0, 0, 0, -1))
        
        self.lifter = CollisionHandlerFloor()
        self.lifter.addCollider(self.fromObject, self.player)
        self.fromObject.show()
        
        self.cTrav = CollisionTraverser()
        self.cTrav.addCollider(self.fromObject, self.lifter)
        self.cTrav.showCollisions(self.render)
        '''
        print(self.player.getTightBounds())
        
    '''
    def hitGround(self, entry):
        print("touching ground")
        print(entry)
        self.player.touchingGround = True
        self.player.setZ(self.scene.model.getZ())
        self.physics.speed = 0
    '''
    
        
        

main = Main()
main.run()

