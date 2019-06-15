import numpy as np
import na2McepClass
import pdb


def dpmatching(d):
    g = np.zeros((d.shape[0], d.shape[1]))
    g[0][0] = d[0][0]

    for i in range(1, d.shape[0]):
        g[i][0] = g[i-1][0] + d[i][0]

    for j in range(1, d.shape[1]):
        g[0][j] = g[0][j-1] + d[0][j]

    for i in range(1, d.shape[0]):
        for j in range(1, d.shape[1]):
            g_temp = np.array([g[i][j-1] + d[i][j], g[i-1][j-1] + 2*d[i][j], g[i-1][j] + d[i][j]])
            g[i][j] = g_temp.min()

    distance_of_words = g[i][j] / (d.shape[0]+d.shape[1])
    return distance_of_words


# main

distance_array = np.load("distance_array.npy")
distance_of_words_array = np.zeros((3,3))

for i in range(distance_array.shape[0]):
    for j in range(distance_array.shape[1]):
        distance_of_words_array[i][j] = dpmatching(distance_array[i][j])

pdb.set_trace()
