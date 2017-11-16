class Camera:
    def __init__(self, num=0):
        from pygame import camera
        camera.init()
        cam = None
        while cam is None:
            cam = camera.Camera(camera.list_cameras()[num])
        self.cam = cam

    def __enter__(self):
        self.cam.start()
        return self.cam

    def __exit__(self, type, value, traceback):
        from pygame import camera
        camera.quit()