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
from src.gamecamera import GameCamera
from src.constants import *
from panda3d.core import loadPrcFileData
#loadPrcFileData("", "want-directtools #t")
#loadPrcFileData("", "want-tk #t")

# Load settings
loadPrcFile('settings.prc')


class Main(ShowBase):
    def __init__(self):
        # TODO: split game update and main into seperate files
        
        ShowBase.__init__(self)

        self.properties = WindowProperties()
        self.properties.setTitle("Dog!")

        self.properties.setIconFilename('assets/textures/animal-dog.ico')
        self.win.requestProperties(self.properties)
        
        # Patch loader to support gltf files
        gltf.patch_loader(self.loader)

        # Disables camera control via mouse (this is required for the camera position to be able to be adjusted in the code)
        self.disableMouse()
        # simplepbr.init()

        #self.debug = Debug()
        self.scene = Level()
        self.player = Player()
        #self.physics = Physics()
        self.movement = Movement()
        self.input = Input()
        self.gamecamera = GameCamera()

        # Create collision traverser
        self.cTrav = CollisionTraverser()
        # Create collision handler to keep player to floor
        # self.floorHandler = CollisionHandlerFloor()
        self.floorHandler = CollisionHandlerGravity()
        self.floorHandler.setGravity(9.81)
        self.floorHandler.setMaxVelocity(14)
        self.wallHandler = CollisionHandlerPusher()

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
        self.floorHandler.addCollider(self.player.avatarRay, self.player.playerNP)
        self.wallHandler.addCollider(self.player.playerCollider, self.player.playerNP)
        # self.floorHandler.setOffset(1.0)

        self.cTrav.addCollider(self.player.avatarRay, self.floorHandler)
        self.cTrav.addCollider(self.player.playerCollider, self.wallHandler)
    
        print(self.player.raygeometry.origin)
        self.player.avatarRay.show()
        self.cTrav.show_collisions(render)
        queue = CollisionHandlerQueue()

        self.cTrav.traverse(render)

        def jump():
            if self.floorHandler.isOnGround():
                
                lf = LerpFunc(lambda t: self.player.playerNP.set_z(t),
                               fromData=self.player.playerNP.get_z(),
                               toData=self.player.playerNP.get_z()+5.0,
                               duration=0.4,
                               blendType='easeOut',
                               extraArgs=[],
                               name=None)
                lf.start()
        self.accept("space", jump)
        print(self.player.model.get_anim_names())
        
        self.accept("1", self.player_spawn)
        self.camLens.set_fov(75)
    def player_spawn(self):
        self.player.playerNP.setPos(self.scene.spawn_point.getPos())

main = Main()
main.run()
