from pygame import surfarray, transform

import numpy as np


def down_scale(img, new_width=28, new_height=28):
    return transform.scale(img, (new_width, new_height))


def gray_scale(img):
    arr = surfarray.array3d(img)
    # luminosity filter
    avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
    arr = np.array([[[avg, avg, avg] for avg in col] for col in avgs])
    return surfarray.make_surface(arr)


def np_gray_scale(gray_scale_surface):
    width, height = gray_scale_surface.get_size()
    return np.array([[gray_scale_surface.get_at((i, j))[0] for j in range(height)] for i in range(width)])
