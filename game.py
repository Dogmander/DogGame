from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
from game.code.player import Player
from game.code.level import Level

from game.code.controls import Input
from game.code.movement import Movement
#from panda3d.core import loadPrcFile
loadPrcFile('settings.prc')

class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Disables camera control via mouse (this is required for the camera position to be able to be adjusted in the code)
        #self.disableMouse()
        
        # Create level
        self.scene = Level()
        self.camera.setPos(0, -15, 1.5)
        self.input = Input()
        self.movement = Movement()
        # Log camera position
        taskMgr.add(self.camera_pos, "camera_pos_task")
        taskMgr.add(self.player_pos, "player_pos_task")
        
        
        taskMgr.add(self.movement.move, "movement_task")
        
        # Create players
        self.player = Player()
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
