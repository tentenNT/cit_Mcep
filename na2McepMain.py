import numpy as np
import na2McepClass
from na2McepClass import WORD_SIZE
import pdb
from joblib import Parallel, delayed
from time import time

# 斜め移動の距離
# SLIDING = 2
SLIDING = np.sqrt(2)

start = time()

# DPマッチングのアルゴリズムを扱う関数
def dpmatching(d):
    g = np.zeros((d.shape[0], d.shape[1]))
    g[0][0] = d[0][0]

    for i in range(1, d.shape[0]):
        g[i][0] = g[i-1][0] + d[i][0]

    for j in range(1, d.shape[1]):
        g[0][j] = g[0][j-1] + d[0][j]

    for i in range(1, d.shape[0]):
        for j in range(1, d.shape[1]):
            g_temp = np.array([g[i][j-1] + d[i][j], g[i-1][j-1] + SLIDING*d[i][j], g[i-1][j] + d[i][j]])
            g[i][j] = g_temp.min()

    distance_of_words = g[i][j] / (d.shape[0]+d.shape[1])
    return distance_of_words


# 何%がラベルと一致しているかを確認する関数
def dw_checker(dw_array):
    count = 0
    label_array = np.array(range(WORD_SIZE))
    ans_array = np.argmin(dw_array, axis=1)

    for x,y in zip(label_array, ans_array):
        if x == y:
            count += 1
        else:
            print("{}番がマッチング失敗".format(x))
    print("{}%正解".format(count))


# main部
distance_array = np.load("distance_array.npy")
distance_of_words_array = np.zeros((WORD_SIZE, WORD_SIZE))
x = 0

for i in range(distance_array.shape[0]):
    q = Parallel(n_jobs=-1)([delayed(dpmatching)(distance_array[i][j]) for j in range(distance_array.shape[1])])
    distance_of_words_array[i, :] = q
#     for j in range(distance_array.shape[1]):
#         distance_of_words_array[i][j] = dpmatching(distance_array[i][j])
    x += 1
    print("{}% done".format(x))

dw_checker(distance_of_words_array)

print("{}秒かかりました".format(time() - start))
