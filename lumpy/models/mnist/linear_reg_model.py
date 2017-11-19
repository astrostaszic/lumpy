import numpy as np
from lumpy.models.mnist.prepare_model import add_bias_feature, sigmoid


def model_from_file(weights_file):
    return Model(np.load(weights_file))


class Model:
    def __init__(self, W):
        self.W = W

    def predict(self, image_2d_np_array):
        image_2d_np_array.resize(1, 784)
        features = add_bias_feature(image_2d_np_array)
        features = np.array([round(f) for f in features[0]])
        sgm = features @ self.W
        print(sgm)
        return np.argmax(sgm)
