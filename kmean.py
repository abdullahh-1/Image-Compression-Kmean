import random
import numpy as np


def unique_randint(k, r):
    return random.sample(range(r), k)


def distance(element, centroids):
    x1, y1, z1 = element[0], element[1], element[2]
    if centroids is None:
        print("...")
        x2, y2, z2 = x1, y1, z1
    else:
        x2, y2, z2 = centroids[0], centroids[1], centroids[2]
    return np.sqrt(np.square(x1 - x2) + np.square(y1 - y2) + np.square(z1 - z2))


def mean(array):
    if len(array) == 0:
        return None

    x, y, z, c = 0, 0, 0, 0
    for i in array:
        c += 1
        x += i[0]
        y += i[1]
        z += i[2]
    return int(x / c), int(y / c), int(z / c)


def closest(means, element):
    value = 0
    index = 0
    x = distance(element, means[0])

    for m in means:
        dis = distance(element, m)
        if x > dis:
            x = dis
            value = index
        index += 1
    return value


def k_mean(array, k):
    x = unique_randint(k, len(array))
    m = [array[i] for i in x]

    while 1:
        g = [[] for _ in range(k)]
        for i in array:
            close = closest(m, i)
            g[close].append(i)
        t = list()
        for i in range(k):
            t.append(mean(g[i]))
        if m == t:
            return m
        m = t


def compress_image(centroids, image):
    for i in range(len(image)):
        image[i] = centroids[closest(centroids, image[i])]
    return image
