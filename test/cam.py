import time

import pygame

from lumpy.img.sources.camera import Camera
from lumpy.img.processing import down_scale, gray_scale, np_gray_scale
# from lumpy.models.mnist.linear_reg_model import model_from_file
from lumpy.models.mnist.nn_model import model_from_file
# from lumpy.models.animals.dogs_cats_keras import model_from_file
import matplotlib.pyplot as plt
import numpy as np
from pygame import surfarray


def run():
    w = 640  # + 280
    h = 480
    size = (w, h)
    screen = pygame.display.set_mode((w, h))
    # model = model_from_file('../lumpy/models/animals/dogs_cats.model')
    model = model_from_file('../lumpy/models/mnist/mnist.keras')

    # ngs = np.zeros((28,28))

    first = True
    with Camera() as cam:
        while True:
            for i in range(7):
                img = cam.get_image()
                ds = down_scale(img)
                gs = gray_scale(ds)
                ngs = (1 - np_gray_scale(gs).T) / 255
                # img = down_scale(img, 150, 150)
                screen.blit(img, (0, 0))
                screen.blit(down_scale(gs, 280, 280), (640, 0))
                pygame.display.flip()  # update the display
                # plt.imshow(ngs, cmap='gray')
                arr = surfarray.array3d(img)
                # print(arr.shape)
                print(model.predict(np.array([arr])))
                print()
                time.sleep(0.1)
                # plt.show(block=False)
                # time.sleep(0.3)
                # plt.close()

                # image.save(img, "original.bmp")
                #
                # ds = down_scale(img)
                # image.save(ds, "down_scale.bmp")
                #
                # gs = gray_scale(ds)
                # image.save(gs, "gray_scale.bmp")
                #
                # print(np.array([[gs.get_at((i, j))[0] for j in range(28)] for i in range(28)]))
