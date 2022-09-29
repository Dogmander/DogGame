# Import dependecies
import gltf


class Level:
    def __init__(self):
        # Patch the loader to support GLTF
        # gltf.patch_loader(loader)

        # Load model and reparent to render
        self.model = loader.loadModel("assets/bam/test.bam")
        self.model.reparentTo(render)
        self.model.set_z(0)
        self.spawn_point = self.model.find("SpawnPoint")
        
        
