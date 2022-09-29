# Import dependencies
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText

# Create Debug class

'''
class Debug:
    def __init__(self):

        base.accept("g", self.toggle)
        self.debug = False
        if self.debug == True:
            self.create()

    def toggle(self):
        if not self.debug:
            self.debug = True
            self.create()
            # base.enable_mouse()
        elif self.debug:
            self.debug = False
            # Remove debugging tasks from task manager
            base.taskMgr.remove("debug_camera_pos")
            base.taskMgr.remove("debug_player_pos")
            base.taskMgr.remove("debug_speed")
            base.taskMgr.remove("debug_touching")
            self.camera_pos_text.destroy()
            self.player_pos_text.destroy()
            self.player_speed_text.destroy()
            self.touching_text.destroy()
            # base.disable_mouse()

    def create(self):
        # Add debugging functions to task manager
        base.taskMgr.add(self.gui_camera_pos, "debug_camera_pos")
        base.taskMgr.add(self.gui_player_pos, "debug_player_pos")
        #base.taskMgr.add(self.gui_speed, "debug_speed")
        #base.taskMgr.add(self.gui_touching, "debug_touching")

        self.camera_pos_text = OnscreenText(
            pos=(-0.5, 0.9), scale=0.1, fg=(1, 0, 0, 1))
        self.player_pos_text = OnscreenText(
            pos=(-0.5, 0.8), scale=0.1, fg=(1, 0, 0, 1))
        self.player_speed_text = OnscreenText(
            pos=(-0.5, 0.7), scale=0.1, fg=(1, 0, 0, 1))
        self.touching_text = OnscreenText(
            pos=(-0.5, 0.6), scale=0.1, fg=(1, 0, 0, 1))

    def gui_camera_pos(self, task):
        pos = base.camera.get_pos()
        # Round values to fit better
        pos = [round(i, 3) for i in pos]
        self.camera_pos_text.setText((f"Camera position: x{pos[0]} y{pos[1]} z{pos[2]}"))
        return Task.cont

    def gui_player_pos(self, task):
        pos = base.playerNP.get_pos()
        # Round values to fit better
        pos = [round(i, 3) for i in pos]
        
        self.player_pos_text.setText((f"Player position: x{pos[0]} y{pos[1]} z{pos[2]}"))
        return Task.cont
    
    def gui_speed(self, task):
        self.player_speed_text.setText(
            f"Vertical speed: {base.physics.speed_vertical}")

        return Task.cont
    
    
    def gui_touching(self, task):
        if base.physics.touching_ground:
            self.touching_text.setText("Touching ground")
        else:
            self.touching_text.setText("Not touching ground")
        return Task.cont
    

'''