import gltf
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import loadPrcFileData
#loadPrcFileData("", "want-directtools #t")
#loadPrcFileData("", "want-tk #t")
class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        gltf.patch_loader(loader)
        #self.scene = loader.loadModel("/d/Other Data/lona.bam")
        #self.scene.reparentTo(render)
        self.actor = Actor("game/assets/models/shibacolor.gltf")
        self.actor.reparentTo(render)
        
main = Main()
main.run()