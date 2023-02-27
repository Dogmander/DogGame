class GameCamera:
    
    def __init__(self):
        base.task_mgr.add(self.update, "cam_update")
    
    def update(self, task):
        base.camera.set_pos(base.player.playerNP, 0, -10, base.player.playerNP.get_z() + 16)
        
        base.camera.set_hpr(base.player.playerNP.get_h(), -45, 0)
        return task.cont