from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
from game.code.player import Player
from game.code.level import Level
from game.code.controls import Mover
#from panda3d.core import loadPrcFile
loadPrcFile('settings.prc')

class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "backward": 0, "jump": 0}
        # Disables camera control via mouse (this is required for the camera position to be able to be adjusted in the code)
        #self.disableMouse()
        
        # Create level
        self.scene = Level()
        self.camera.setPos(0, -15, 1.5)
        self.mover = Mover()
        # Log camera position
        taskMgr.add(self.camera_pos, "camera_pos_task")
        taskMgr.add(self.player_pos, "player_pos_task")
        
        self.accept("w", self.setKey, ["forward", True])
        self.accept("s", self.setKey, ["backward", True])
        self.accept("a", self.setKey, ["left", True])
        self.accept("d", self.setKey, ["right", True])
        self.accept("w-up", self.setKey, ["forward", False])
        self.accept("s-up", self.setKey, ["backward", False])
        self.accept("a-up", self.setKey, ["left", False])
        self.accept("d-up", self.setKey, ["right", False])
        taskMgr.add(self.mover.rotation, "rotation_task")
        
        # Create players
        self.player = Player()
        self.player2 = Player()
        
        # Move second player to the right so it doesn't clip into first player
        self.player2.setPos(2, 0, 0)
        
        # Animations for testing
        #self.player.loop("Walk")
        self.player2.loop("Gallop")
        
        # Add temporary lights, these will be replaced when I figure out better lighting    
        dlight = DirectionalLight('my dlight')
        dlnp = self.render.attachNewNode(dlight)
        dlight.setColor((1, 1, 1, 1))
        dlnp.setHpr(0, -5, 0)
        self.render.setLight(dlnp)
        
        self.camera_pos_text = OnscreenText(pos=(-0.5, 0.9), scale=0.1, fg=(1, 0, 0, 1))
        self.player_pos_text = OnscreenText(pos=(-0.5, 0.8), scale=0.1, fg=(1, 0, 0, 1))
    
    
    def setKey(self, key, value):
        self.keyMap[key] = value
        
    
        
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
main = Main()
main.run()
