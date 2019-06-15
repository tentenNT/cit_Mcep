import numpy as np
import na2McepClass as mclass
from na2McepClass import WORD_SIZE
import pdb


# フレーム同士での局所間距離計算を行う関数
def distance_checker(template_data, test_data):
    print(template_data.word, test_data.word)
    distance_array_frames = np.zeros((len(template_data.framedata), len(test_data.framedata)))

    for i in range(len(template_data.framedata)):
        for j in range((len(test_data.framedata))):
            distance_array_frames[i][j] = np.linalg.norm(template_data.framedata[i] - test_data.framedata[j])

    return distance_array_frames


# main部
template_data_list = mclass.readfiles(mclass.template_data_location)
test_data_list = mclass.readfiles(mclass.test_data_location)

# 例: print(template_data_list[2].framedata[0][4])
# これでcity011_003.textの0フレーム目の3次元目を指す

# 単語同士を行列に並べる
distance_list = [[] for i in range(WORD_SIZE)]
for i, template_data in enumerate(template_data_list[:WORD_SIZE]):
    for j, test_data in enumerate(test_data_list[:WORD_SIZE]):
        distance_list[i].append(distance_checker(template_data, test_data)) # appendを使うのでjは不要
distance_array = np.array(distance_list)

# 毎回計算すると大変なのでnpy形式で全ての単語同士での局所間距離を保存
np.save("distance_array.npy", distance_array)
