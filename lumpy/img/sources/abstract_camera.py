from abc import ABC, abstractmethod


class Camera(ABC):

    @abstractmethod
    def __init__(self, num=0, size=(640, 640)):
        pass

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass
