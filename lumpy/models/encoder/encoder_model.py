import numpy as np
from lumpy.img.sources import camera
import pygame
import matplotlib.pyplot as plt
from skimage import io


def k_means_iteration(centroids, datapoints):
    c_t = np.array([c.reshape(-1, 1) for c in centroids.T])
    d_t = np.array([d.reshape(-1, 1) for d in datapoints.T])

    diffs = np.array([
        (c_t[i].reshape(-1) ** 2 - 2 * (d_t[i].dot(c_t[i].T))).T + d_t[i].reshape(-1) ** 2
        for i in range(len(c_t))])

    diffs = diffs.sum(axis=0)

    cluster_assignments = np.argmin(diffs, axis=0)
    clusters = np.array([np.argwhere(cluster_assignments == i) for i in range(len(centroids))])
    c_t = np.array(
        [
            [
                d_t[i][c].mean() if d_t[i][c].size != 0 else d_t[i].mean() for c in clusters
            ]
            for i in range(len(c_t))
        ])

    return c_t.T, clusters


def k_means_img_compression(num_iterations, centroids, image):
    datapoints = np.copy(image.reshape(-1, 3))
    _, clusters = k_means_iteration(centroids, datapoints)
    for i in range(num_iterations):
        centroids, clusters = k_means_iteration(centroids, datapoints)

    for i in range(len(clusters)):
        datapoints[clusters[i]] = centroids[i]
    img_reconstructed = datapoints.reshape(image.shape)
    print(num_iterations)
    return img_reconstructed, clusters


def main():
    num_centroids = 24
    centroids = np.random.rand(num_centroids, 3) * 255

    with camera.Camera(0) as cam:
        w = 640  # *2
        h = 480  # *2
        size = (w, h)
        screen = pygame.display.set_mode((w, h))
        # while True:
        # img = cam.get_image()
        img = pygame.image.load('avengers.png')
        screen.blit(img, (0, 0))
        pygame.display.flip()
        img = pygame.transform.rotate(img, 90)
        arr = pygame.surfarray.pixels3d(img)
        print(arr.shape)
        comp, clusters = k_means_img_compression(5, centroids, arr)

        pygame.image.save(img, 'photo.jpg')
        io.imsave('photo.png', arr)
        io.imsave('photo.jpg', arr)
        io.imsave('photo.bmp', arr)

        io.imsave(('photo_comp_' + str(num_centroids) + '.png'), comp)
        # f = open('test.txt', 'w+', encoding='byte')
        # f.write(clusters)
        # f.close()
        np.save('photo_clusters', clusters)

        np.save('comp.txt', comp)
        plt.imshow(comp)
        plt.show()
        # print(clusters)
        print(clusters.shape)
        print()

    # recons = pygame.surfarray.make_surface(comp)
    #
    #
    # screen.blit(recons, (w, h))
    # pygame.display.flip()

    # input('xD')
# print(img.shape)
# # plt changes the rgb channels order...
# plt.imshow(img[:,:,[2,1,0]])
