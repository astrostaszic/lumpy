import time

import pygame

from lumpy.img.sources.camera import Camera
# from lumpy.models.mnist.linear_reg_model import model_from_file
from lumpy.models.mnist.nn_model import model_from_file
# from lumpy.models.animals.dogs_cats_keras import model_from_file



def main():
    w = 640 + 280
    h = 480
    size = (w, h)
    screen = pygame.display.set_mode((w, h))
    # model = model_from_file('./lumpy/models/animals/dogs_cats.model')
    model = model_from_file('./lumpy/models/mnist/mnist.keras')
    # model = model_from_file('./lumpy/models/mnist/linreg.npy')

    with Camera() as cam:
        while True:
            start = time.time()
            img = cam.get_image()
            screen.blit(img, (0, 0))
            pygame.display.flip()
            pred = model.predict(img)
            stop = time.time()
            print(pred, format(stop - start, '.3f'))
            time.sleep(0.1)



main()