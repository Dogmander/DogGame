# Import dependecies
import gltf
import sys

class Level:
    def __init__(self):
        # Patch the loader to support GLTF
        # gltf.patch_loader(loader)

        # Load model and reparent to render
        try:
            self.model = loader.loadModel(sys.argv[1]) # Load level from provided file
        except IndexError:
            self.model = loader.loadModel("assets/bam/test.bam") # Load default level if no level provided
        
        self.model.reparentTo(render)
        self.model.set_z(0)
        self.spawn_point = self.model.find("SpawnPoint")
        
        
