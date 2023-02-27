# Import dependencies

from direct.task import Task
from direct.gui.OnscreenText import OnscreenText

# Create Debug class

class Debug:
    def __init__(self):
        debug_font = loader.loadFont("assets/fonts/Hack-Regular.ttf")
        self.player_text = OnscreenText(
            pos=(0, 0.9), scale=0.05, font=debug_font
        )
        self.camera_text = OnscreenText(
            pos=(0, 0.8), scale=0.05, font=debug_font
        )
        self.ground_text = OnscreenText(
            pos=(0, 0.7), scale=0.05, font=debug_font
        )
        base.task_mgr.add(self.update, 'debug_update')

    def update(self, task):
        # Round values to 3 decimals to fit better onscreen
        def format(pos):
            return [round(i, 3) for i in pos]
        
        player_pos = format(base.player.playerNP.get_pos())
        player_rot = format(base.player.playerNP.get_hpr())
        self.player_text.setText(
            f"Player position: x {player_pos[0]} y {player_pos[1]} z {player_pos[2]} Player rotation: h {player_rot[0]} p {player_rot[1]} r {player_rot[2]}"
        )
        
        camera_pos = format(base.camera.get_pos())
        self.camera_text.setText(f"Camera position: x {camera_pos[0]} y {camera_pos[1]} z {camera_pos[2]}")
        
        self.ground_text.setText(f"Touching ground: {base.floorHandler.is_on_ground()}")
        
        return Task.cont
