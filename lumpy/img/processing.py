from pygame import surfarray, transform

import numpy as np
import pygame


def rescale(img, new_width=28, new_height=28):
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


def np_grayscaled_to_img(np_array):
    img = 255 * np_array.T / np_array.max()
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 2] = ret[:, :, 1] = ret[:, :, 0] = img
    surf = surfarray.make_surface(ret)
    return surf
