import numpy as np
from lumpy.models.mnist.prepare_model import add_bias_feature, sigmoid
from lumpy.img.processing import rescale, gray_scale, np_gray_scale, np_to_img
import pygame
import matplotlib.pyplot as plt

def model_from_file(weights_file):
    return Model(np.load(weights_file))


class Model:
    def __init__(self, W):
        self.W = W

    def dump_to_screen(self, grayscaled):
        w = 640 + 280
        h = 480
        screen = pygame.display.set_mode((w, h))
        screen.blit(rescale(grayscaled, 280, 280), (640, 0))

    def process(self, image, verbose=True):
        ds = rescale(image, 28, 28)
        gs = gray_scale(ds)

        ngs = 1 - (np_gray_scale(gs).T) / 255
        # ngs = ngs.round()
        if verbose:
            self.dump_to_screen(np_to_img(ngs))
            plt.show()
        features = add_bias_feature(ngs.reshape(1, 784))
        # features = np.array([round(f) for f in features[0]])
        return features

    def predict(self, image):
        features = self.process(image)
        sgm = features @ self.W
        return np.argmax(sgm)
