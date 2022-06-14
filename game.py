from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
from game.code.player import Player
from game.code.level import Level

from panda3d.core import loadPrcFileData
from panda3d.core import loadPrcFile
#loadPrcFileData("", "want-directtools #t")
#loadPrcFileData("", "want-tk #t")
loadPrcFile(Filename.expand_from('$MAIN_DIR/Config.prc'))


class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        #self.disableMouse()
        
        # Create level
        self.scene = Level()
        
        # Create players
        self.player = Player()
        self.player2 = Player()
        
        self.player2.setPos(2, 0, 0)
        
        self.player.loop("Walk")
        self.player2.loop("Gallop")
        # Apply scale and position transforms on the model.
        #self.scene.setScale(0.25, 0.25, 0.25)
        #self.scene.setPos(-8, 42, 0)
        dlight = DirectionalLight('my dlight')
        dlnp = self.render.attachNewNode(dlight)
        
        dlight.setColor((1, 1, 1, 1))
        dlnp.setHpr(0, -60, 0)
        dlnp.setPos(0, 20, 0)
        
        self.render.setLight(dlnp)
        self.textObject = OnscreenText(text="Hello World", pos=(0.5, 0.8), scale=0.1, fg=(1, 0, 0, 1))
       
main = Main()
main.run()
