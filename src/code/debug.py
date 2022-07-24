# Import dependencies
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText

# Create Debug class


class Debug:
    def __init__(self):
        # Add toggle keybind
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
        base.taskMgr.add(self.gui_speed, "debug_speed")
        base.taskMgr.add(self.gui_touching, "debug_touching")

        self.camera_pos_text = OnscreenText(
            pos=(-0.5, 0.9), scale=0.1, fg=(1, 0, 0, 1))
        self.player_pos_text = OnscreenText(
            pos=(-0.5, 0.8), scale=0.1, fg=(1, 0, 0, 1))
        self.player_speed_text = OnscreenText(
            pos=(-0.5, 0.7), scale=0.1, fg=(1, 0, 0, 1))
        self.touching_text = OnscreenText(
            pos=(-0.5, 0.6), scale=0.1, fg=(1, 0, 0, 1))

    def gui_camera_pos(self, task):
        x = str(round(base.camera.getX(), 3))
        y = str(round(base.camera.getY(), 3))
        z = str(round(base.camera.getZ(), 3))

        self.camera_pos_text.setText((f"Camera position: x{x} y{y} z{z}"))
        return Task.cont

    def gui_player_pos(self, task):
        x = str(round(base.player.getX(), 3))
        y = str(round(base.player.getY(), 3))
        z = str(round(base.player.getZ(), 3))

        self.player_pos_text.setText((f"Player position: x{x} y{y} z{z}"))
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
