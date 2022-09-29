# Import dependencies

from panda3d.core import *
from panda3d.core import WindowProperties

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.LerpInterval import LerpFunc

import simplepbr
import gltf

from src.player import Player
from src.level import Level
from src.debug import Debug
from src.controls import Input
from src.movement import Movement
from src.physics import Physics

# from panda3d.core import loadPrcFileData
# loadPrcFileData("", "want-directtools #t")
# loadPrcFileData("", "want-tk #t")

# Load settings
loadPrcFile('settings.prc')


class Main(ShowBase):
    def __init__(self):
        # TODO: split game update and main into seperate files
        
        ShowBase.__init__(self)

        self.properties = WindowProperties()
        self.properties.setTitle("Dog!")

        self.properties.setIconFilename('assets/textures/animal-dog.bmp')
        self.win.requestProperties(self.properties)
        
        # Patch loader to support gltf files
        gltf.patch_loader(self.loader)

        # Disables camera control via mouse (this is required for the camera position to be able to be adjusted in the code)
        # self.disableMouse()
        # simplepbr.init()

        
        self.debug = Debug()
        self.scene = Level()
        self.player = Player()
        #self.physics = Physics()
        self.movement = Movement()
        self.input = Input()

        self.music = self.loader.loadMusic(
            "src/assets/sound/Sneaky Adventure.mp3")
        self.music.setVolume(0.1)
        # self.music.play()

        # self.player2 = Player()

        # Move second player to the right so it doesn't clip into first player
        # self.player2.setPos(2, 0, 0)

        # Animations for testing

        # self.player2.loop("Gallop")


        # Create collision traverser
        self.cTrav = CollisionTraverser()
        # Create collision handler to keep player to floor
        # self.floorHandler = CollisionHandlerFloor()
        self.floorHandler = CollisionHandlerGravity()
        self.floorHandler.setGravity(9.81)
        self.floorHandler.setMaxVelocity(14)
        self.wallHandler = CollisionHandlerPusher()
        FLOOR_MASK = BitMask32.bit(1)
        WALL_MASK = BitMask32.bit(2)

        self.playerNP = NodePath('playerNP')
        self.playerNP.reparentTo(self.render)

        self.player.model.reparentTo(self.playerNP)
        self.player.model.setCollideMask(BitMask32.allOff())

        
        self.playerNP.setPos(0, 0, 15)
        
        self.playerCollider = self.player.model.attachNewNode(
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

        self.scene.model.setCollideMask(BitMask32.allOff())
        # self.scene.model.setScale(10)

        self.floorcollider = self.scene.model.find(
            "**/Ground_collision/Ground_collision")
        self.wallcollider = self.scene.model.find(
            "**/Wall_collision/Wall_collision")
        self.wallcollider.node().setIntoCollideMask(WALL_MASK)

        # print(self.scene.model.find("**/floor_collide"))
        # print(self.scene.model.find("**/Plane_collision/Plane_collision"))
        self.floorcollider.node().setIntoCollideMask(FLOOR_MASK)
        self.floorcollider.show()
        self.floorHandler.addCollider(self.avatarRay, self.playerNP)
        self.wallHandler.addCollider(self.playerCollider, self.playerNP)
        # self.floorHandler.setOffset(1.0)

        self.cTrav.addCollider(self.avatarRay, self.floorHandler)
        self.cTrav.addCollider(self.playerCollider, self.wallHandler)

      
        self.accept('h', print, [self.playerNP.getPos()])
        
        print(self.player.model.list_joints())
        
        # myNodePath = self.player.expose_joint(None, "modelRoot", "Head")
        # ball = self.loader.loadModel("models/panda.egg.pz")
        # ball.reparentTo(myNodePath)

        # self.accept('p', print, [ball.getPos()])
        #self.accept('j', self.playerNP.setZ, [1])
        #self.accept('u', self.playerNP.setZ, [self.playerNP, 5])
        #self.accept('l', lambda: print, [self.avatarRay.node().getOrigin()])
        print(self.raygeometry.origin)
        self.avatarRay.show()
        self.cTrav.show_collisions(render)
        queue = CollisionHandlerQueue()

        self.cTrav.traverse(render)

        def ground(task):
            print(self.floorHandler.isOnGround())
            return Task.cont
        #self.task_mgr.add(ground)

        def jump():
            if self.floorHandler.isOnGround():
                
                lf = LerpFunc(lambda t: self.playerNP.set_z(t),
                               fromData=self.playerNP.get_z(),
                               toData=self.playerNP.get_z()+5.0,
                               duration=0.4,
                               blendType='easeOut',
                               extraArgs=[],
                               name=None)
                lf.start()
        self.accept("space", jump)
        print(self.player.model.get_anim_names())


main = Main()
main.run()
