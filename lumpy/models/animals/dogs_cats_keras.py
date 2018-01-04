import numpy as np
from tensorflow import keras
import pygame
from lumpy.img.processing import rescale


def model_from_file(model_file):
    return Model(keras.models.load_model(model_file))


class Model:
    def __init__(self, model):
        self.model = model

    def predict(self, image):
        img = pygame.transform.rotate(rescale(image, 150, 150), 90)
        arr = pygame.surfarray.pixels3d(img)
        image_2d_np_array = arr
        predict = self.model.predict(np.expand_dims(image_2d_np_array,0))
        return predict
