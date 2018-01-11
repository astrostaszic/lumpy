import numpy as np
from lumpy.models.mnist.prepare_model import add_bias_feature, sigmoid
from lumpy.img.processing import rescale, gray_scale, np_gray_scale, np_grayscaled_to_img
import pygame

from tensorflow.contrib import keras


def model_from_file(model_file):
    return Model(keras.models.load_model(model_file))


class Model:
    def __init__(self, model):
        self.model = model

    def dump_to_screen(self, grayscaled):
        w = 640 + 280
        h = 480
        screen = pygame.display.set_mode((w, h))
        screen.blit(rescale(grayscaled, 280, 280), (640, 0))

    def process(self, image, verbose=True):
        ds = rescale(image, 28, 28)
        gs = gray_scale(ds)

        ngs = 1 - (np_gray_scale(gs).T) / 255
        ngs *= (ngs > 0.6).astype(int)

        if verbose:
            self.dump_to_screen(np_grayscaled_to_img(ngs))
            # plt.show()
        features = ngs.reshape(784)
        # features = np.array([round(f) for f in features[0]])
        return features

    def predict(self, image):
        features = self.process(image)

        predict = self.model.predict(np.array([features]))
        print(predict)
        return np.argmax(predict)

    # def predict(self, image_2d_np_array):
    #     width, height = image_2d_np_array.shape
    #     image_2d_np_array.resize(width * height)
    #     predict = self.model.predict(np.array([image_2d_np_array]))
    #     print(predict)
    #     return np.argmax(predict)
