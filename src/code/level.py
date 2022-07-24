# Import dependecies
import gltf

class Level:
    def __init__(self):
        # Patch the loader to support GLTF
        #gltf.patch_loader(loader)
        
        # Load model and reparent to render
        self.model = loader.loadModel("src/assets/models/slope2.bam")
        self.model.reparentTo(render)
