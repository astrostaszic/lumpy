import time

import pygame

from lumpy.img.sources.pygame_camera import PygameCamera
from lumpy.img.processing import rescale, gray_scale, np_gray_scale
from lumpy.models.mnist.linear_reg_model import model_from_file
# from lumpy.models.mnist.nn_model import model_from_file
# from lumpy.models.animals.dogs_cats_keras import model_from_file
# import matplotlib.pyplot as plt
import numpy as np
from pygame import surfarray


def main():
    w = 640 + 280
    h = 480
    size = (w, h)
    screen = pygame.display.set_mode((w, h))
    # model = model_from_file('../lumpy/models/animals/dogs_cats.model')
    # model = model_from_file('../lumpy/models/mnist/mnist.keras')
    model = model_from_file('../lumpy/models/mnist/linreg.npy')

    first = True
    l = []
    with PygameCamera() as cam:
        while True:
            time_1 = time.time()
            img = cam.get_image()
            time_2 = time.time()
            screen.blit(img, (0, 0))
            pygame.display.flip()
            time_3 = time.time()
            pred = model.predict(img)
            time_4 = time.time()
            l.append((time_2 - time_1, time_4 - time_3))
            print(pred)
            print()
            #time.sleep(0.1)
