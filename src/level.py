# Import dependecies
import sys
from panda3d.core import Filename

class Level:
    def __init__(self):

        # Load model and reparent to render
        if len(sys.argv) >= 2:
            self.model = loader.loadModel(Filename.fromOsSpecific(sys.argv[1]))
        else:
            self.model = loader.loadModel("assets/bam/test.bam")
        
        self.model.reparentTo(render)
        self.model.set_z(0)
        self.spawn_point = self.model.find("SpawnPoint")
        
        
