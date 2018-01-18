from lumpy.img.sources.abstract_camera import Camera
import picamera


class PiCamera(Camera):
    def __init__(self, num=0, size=(640, 640)):
        super().__init__(num, size)
        self.cam = picamera.PiCamera()

    def __enter__(self):
        self.cam.start()
        return self.cam

    def __exit__(self, type, value, traceback):
        from pygame import camera
        camera.quit()
