# Import dependencies

from panda3d.core import *
from panda3d.core import WindowProperties
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText

import simplepbr
import gltf

from src.code.player import Player
from src.code.level import Level
from src.code.debug import Debug
from src.code.controls import Input
from src.code.movement import Movement
from src.code.physics import Physics

#from panda3d.core import loadPrcFileData
# loadPrcFileData("", "want-directtools #t")
# loadPrcFileData("", "want-tk #t")

# Load settings
loadPrcFile('settings.prc')



class Main(ShowBase):
    def __init__(self):

        ShowBase.__init__(self)
        self.properties = WindowProperties()
        self.properties.setTitle("Dog!")
        
        self.properties.setIconFilename('src/assets/textures/animal-dog.ico')
        base.win.requestProperties(self.properties)
        
        # Patch loader to support gltf files
        gltf.patch_loader(loader)

        # Disables camera control via mouse (this is required for the camera position to be able to be adjusted in the code)
        # self.disableMouse()
        # simplepbr.init()

        self.debug = Debug()
        self.scene = Level()
        self.player = Player()
        self.physics = Physics()
        self.movement = Movement()
        self.input = Input()

        self.music = loader.loadMusic("src/assets/sound/Sneaky Adventure.mp3")
        self.music.setVolume(0.1)
        self.music.play()

        self.player2 = Player()

        # Move second player to the right so it doesn't clip into first player
        self.player2.setPos(2, 0, 0)

        # Animations for testing
        
        self.player2.loop("Gallop")
        print(self.scene.model.find('Plane'))
        print(self.scene.model.getTightBounds())
        '''
        # render.setShaderAuto()
        self.cTrav = CollisionTraverser()

        self.pnodePath = self.scene.model.attachNewNode(CollisionNode('pnode'))
        self.pnodePath.node().addSolid(CollisionPolygon(Point3(-10, -10, 0), Point3(10, -10, 0),
                                                        Point3(10, 10, 0), Point3(-10, 10, 0)))
        self.scene.model.node().setIntoCollideMask(CollideMask.bit(0))
        print(self.scene.model.getTightBounds())

        self.pnodePath.show()
        # self.scene.model.find("Plane").node().setIntoCollideMask(BitMask32(0x10))
        self.playerCol = CollisionNode('playerCol')
        #self.playerCol.addSolid(CollisionSphere(0, 0, 1, 0.5))
        self.playerCol.addSolid(CollisionSphere(0, -1, 1.2, 1.25))
        self.playerCol.addSolid(CollisionSphere(0, 0.5, 1.2, 1.25))
        self.playerCol.setFromCollideMask(CollideMask.bit(0))
        self.playerCol.setIntoCollideMask(CollideMask.allOff())
        self.playerColNp = self.player.attachNewNode(self.playerCol)
        self.playerPusher = CollisionHandlerPusher()
        self.playerPusher.horizontal = False

        self.playerPusher.addCollider(self.playerColNp, self.player)
        self.cTrav.addCollider(self.playerColNp, self.playerPusher)
        self.playerColNp.show()
        self.cTrav.showCollisions(render)
        # print(self.cTrav.getColliders())

        taskMgr.add(base.physics.gravity, "gravity_task")
        #taskMgr.add(self.physics.test, "test")
        self.playerPusher.addInPattern('player-in-pnode')
        self.playerPusher.addOutPattern('player-out-pnode')
        self.playerPusher.addAgainPattern('player-again-pnode')

        #self.accept('player-into-pnode', self.hitGround)
        self.accept('player-in-pnode', self.physics.groundState, [True])
        self.accept('player-out-pnode', self.physics.groundState, [False])
        self.accept('player-again-pnode', self.physics.groundState, [True])
        lifter = CollisionHandlerFloor()
        lifter.addCollider(self.playerColNp, self.player)
        '''
        # Create collision traverser
        self.cTrav=CollisionTraverser()
        # Create collision handler to keep player to floor
        self.floorHandler = CollisionHandlerFloor()
        self.floorHandler.setMaxVelocity(14)
        self.wallHandler = CollisionHandlerPusher()
        FLOOR_MASK=BitMask32.bit(1)
        WALL_MASK=BitMask32.bit(2)
        
        self.playerNP=NodePath('playerNP')
        self.playerNP.reparentTo(base.render)
        self.player.reparentTo(self.playerNP)
        self.player.setCollideMask(BitMask32.allOff())
        self.playerNP.setZ(15)
        self.player.setZ(1)
        
        self.playerCollider = self.player.attachNewNode(CollisionNode('playercnode'))
        self.playerCollider.node().addSolid(CollisionSphere(0, -1, 1.2, 1))
        self.playerCollider.node().addSolid(CollisionSphere(0, 1.25, 1.2, 1.25))
        self.playerCollider.show()
        self.playerCollider.node().setFromCollideMask(WALL_MASK)
        self.playerCollider.node().setIntoCollideMask(BitMask32.allOff())
        
        self.raygeometry = CollisionRay(0, 0, 2, 0, 0, -1)
        self.avatarRay = self.player.attachNewNode(CollisionNode('avatarRay'))
        self.avatarRay.node().addSolid(self.raygeometry)
        self.avatarRay.node().setFromCollideMask(FLOOR_MASK)
        self.avatarRay.node().setIntoCollideMask(BitMask32.allOff())
        self.scene.model.setCollideMask(BitMask32.allOff())
        #self.scene.model.setScale(10)
        self.floorcollider=self.scene.model.find("**/Ground_collision/Ground_collision")
        self.wallcollider=self.scene.model.find("**/Wall_collision/Wall_collision")
        self.wallcollider.node().setIntoCollideMask(WALL_MASK)
        self.wallcollider.show()
        #print(self.scene.model.find("**/floor_collide"))
        #print(self.scene.model.find("**/Plane_collision/Plane_collision"))
        self.floorcollider.node().setIntoCollideMask(FLOOR_MASK)
        self.floorcollider.show()
        self.floorHandler.addCollider(self.avatarRay, self.playerNP)
        self.wallHandler.addCollider(self.playerCollider, self.playerNP)
        self.floorHandler.setOffset(1.0)
        self.cTrav.addCollider(self.avatarRay, self.floorHandler)
        self.cTrav.addCollider(self.playerCollider, self.wallHandler)
        self.accept('h', print, [self.playerNP.getZ()])
        

main = Main()
main.run()
