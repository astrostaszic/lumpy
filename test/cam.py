from pygame import camera, image
import pygame
import numpy as np


def grayscale(img):
    arr = pygame.surfarray.array3d(img)
    #luminosity filter
    avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
    arr = np.array([[[avg,avg,avg] for avg in col] for col in avgs])
    return pygame.surfarray.make_surface(arr)

camera.init()
cam = None
while cam is None:
    print(1)
    cam = camera.Camera(camera.list_cameras()[0])

cam.start()
img = cam.get_image()

resized = pygame.transform.scale(img, (28,28))
image.save(img, "photo.bmp")

image.save(resized, "resized.bmp")

gr = grayscale(resized)


image.save(gr, "greyscale.bmp")

print(np.array([[gr.get_at((i, j))[0] for j in range(28)] for i in range(28)]))


camera.quit()
