from pygame import surfarray, transform

import numpy as np


def gray_scale(img):
    arr = surfarray.array3d(img)
    # luminosity filter
    avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
    arr = np.array([[[avg, avg, avg] for avg in col] for col in avgs])
    return surfarray.make_surface(arr)


def down_scale(img):
    return transform.scale(img, (28, 28))
