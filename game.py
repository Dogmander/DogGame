from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
from game.code.player import Player
from game.code.level import Level

from game.code.controls import Input
from game.code.movement import Movement
from game.code.physics import Physics
#from panda3d.core import loadPrcFileData
#loadPrcFileData("", "want-directtools #t")
#loadPrcFileData("", "want-tk #t")


loadPrcFile('settings.prc')

class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Disables camera control via mouse (this is required for the camera position to be able to be adjusted in the code)
        #self.disableMouse()
        
        # Create level
        self.scene = Level()
        self.camera.setPos(0, -15, 1.5)
        #self.input = Input()
        self.movement = Movement()
        self.physics = Physics()
        # Log camera position
        taskMgr.add(self.camera_pos, "camera_pos_task")
        taskMgr.add(self.player_pos, "player_pos_task")
        taskMgr.add(self.speed_text, "speed_text_task")
        
        taskMgr.add(self.movement.move, "movement_task")
        
        # Create players
        self.player = Player()
        self.player.setZ(25)
        self.player2 = Player()
        print(self.player.getAnimNames())
        # Move second player to the right so it doesn't clip into first player
        self.player2.setPos(2, 0, 0)
        
        # Animations for testing
        #self.player.loop("Idle")
        self.player2.loop("Gallop")
        
        # Add temporary lights, these will be replaced when I figure out better lighting    
        dlight = DirectionalLight('my dlight')
        dlnp = self.render.attachNewNode(dlight)
        dlight.setColor((1, 1, 1, 1))
        dlnp.setHpr(0, -5, 0)
        self.render.setLight(dlnp)
        
        self.camera_pos_text = OnscreenText(pos=(-0.5, 0.9), scale=0.1, fg=(1, 0, 0, 1))
        self.player_pos_text = OnscreenText(pos=(-0.5, 0.8), scale=0.1, fg=(1, 0, 0, 1))
        self.player_speed_text = OnscreenText(pos=(-0.5, 0.7), scale=0.1, fg=(1, 0, 0, 1))
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
   
    
        self.physics.touchingGround = False
        #taskMgr.add(base.physics.gravity, "gravity_task")
        self.playerPusher.addInPattern('player-into-pnode')
        #taskMgr.add(base.player.physics, "physics")
        #self.accept('player-into-pnode', self.hitGround)
        self.accept('player-into-pnode', self.physics.hitGround)

        
        taskMgr.add(self.falsify, "falsify_task", sort=29)
    
    def falsify(self, task):
        self.physics.touchingGround = False
        
        return Task.cont   
    
    def hitGround(self, entry):
        print("touching ground")
        print(entry)
        self.player.touchingGround = True
        self.player.setZ(self.scene.model.getZ())
        self.physics.speed = 0
    

        
        
    def camera_pos(self, task):
        x = str(round(self.camera.getX(), 3))
        y = str(round(self.camera.getY(), 3))
        z = str(round(self.camera.getZ(), 3))
        
        self.camera_pos_text.setText((f"Camera position: x{x} y{y} z{z}"))
        return Task.cont
    def player_pos(self, task):
        x = str(round(self.player.getX(), 3))
        y = str(round(self.player.getY(), 3))
        z = str(round(self.player.getZ(), 3))
        
        self.player_pos_text.setText((f"Player position: x{x} y{y} z{z}"))
        return Task.cont
    def speed_text(self, task):
        speed = str(round(self.physics.current_speed, 3))
        self.player_speed_text.setText((f"Player speed: {speed}"))
        print(self.physics.touchingGround)
        return Task.cont
    
main = Main()
main.run()
