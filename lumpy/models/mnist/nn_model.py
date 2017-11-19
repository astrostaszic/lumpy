import numpy as np
from tensorflow.contrib import keras


def model_from_file(model_file):
    return Model(keras.models.load_model(model_file))


class Model:
    def __init__(self, model):
        self.model = model

    def predict(self, image_2d_np_array):
        width, height = image_2d_np_array.shape
        image_2d_np_array.resize(width * height)
        predict = self.model.predict(np.array([image_2d_np_array]))
        print(predict)
        return np.argmax(predict)
