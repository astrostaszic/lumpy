from pygame import camera, image

camera.init()
cam = None
while cam is None:
    print(1)
    cam = camera.Camera(camera.list_cameras()[0])

cam.start()
img = cam.get_image()
image.save(img, "photo.bmp")
camera.quit()
