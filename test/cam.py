from pygame import image

from test.utils import down_scale, gray_scale
from test.with_camera import Camera
import numpy as np

with Camera() as cam:
    img = cam.get_image()

image.save(img, "original.bmp")

ds = down_scale(img)
image.save(ds, "down_scale.bmp")

gs = gray_scale(ds)
image.save(gs, "gray_scale.bmp")

print(np.array([[gs.get_at((i, j))[0] for j in range(28)] for i in range(28)]))
