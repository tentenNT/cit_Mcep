import numpy as np
import na2McepFunctions as mfunc
import na2McepClass as mclass
import pdb

def distance_checker(template_data, test_data): # フレーム同士での計算
    print(template_data.word, test_data.word)
#     pdb.set_trace()
    distance_array = np.zeros((len(template_data.framedata), len(test_data.framedata))) # タプルで渡す
# 5フレーム用
#     distance_array = np.zeros((5, 5)) # タプルで渡す
    for i in range(len(template_data.framedata)):
# こっちだと5フレーム分だけ計算する
#     for i in range(5):
        for j in range((len(test_data.framedata))):
# 上に同じ
#         for j in range(5):
#             print(i, j, np.linalg.norm(template_data.framedata[i] - test_data.framedata[j]))
            distance_array[i][j] = np.linalg.norm(template_data.framedata[i] - test_data.framedata[j])
#             print(distance_array)
#             pdb.set_trace()

# リスト内包表記にしてみる
#     distance_array = [print(i, j, np.linalg.norm(template_data.framedata[i] - test_data.framedata[j])) for i in range(len(template_data.framedata)) for j in range(len(test_data.framedata))]
#     distance_array[:] = [np.linalg.norm(template_data.framedata[i] - test_data.framedata[j]) for i in range(len(template_data.framedata)) for j in range(len(test_data.framedata))]
# できねえ

#     print(distance_array)
    return distance_array

# a_array = np.ndarray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# b_array = np.ndarray([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 11, 12, 13, 14, 15])
# print(mfunc.local_distance(a_array, b_array))
# np.linalg.norm(a_array-b_array)

template_data_list = mclass.readfiles(mclass.template_data_location)
test_data_list = mclass.readfiles(mclass.test_data_location)
# print(template_data_list[2].framedata[0][4])
# こうすればcity011_003.textの0フレーム目の3次元目が取れる

# うっかり同じワード同士の比較しかやっていなかった
# これでは意味がない…DPマッチングするためには全部計算する必要がある
# for template_data, test_data in zip(template_data_list, test_data_list): というミス

# 単語同士でのマッチング
# distance_array = np.zeros((100, 100))
# distance_array = np.zeros((5, 5))
distance_list = []
distance_list_inside = []
# フルサイズ(100*100)
for template_data in template_data_list:
    for test_data in test_data_list:
        distance_checker(template_data, test_data)

# 3*3サイズ
# for template_data in template_data_list[:3]:
#     for test_data in test_data_list[:3]:
#         distance_list_inside.append(distance_checker(template_data, test_data))
#     distance_list.append(distance_list_inside)

# リスト内包表記にしてみる(100*100)
# 次元を間違っている
# print(distance_array)
# distance_list = [distance_checker(template_data, test_data) for template_data in template_data_list for test_data in template_data_list]
# リスト内包表記にしてみる(5*5)
# distance_list = [distance_checker(template_data, test_data) for template_data in template_data_list[:5] for test_data in test_data_list[:5]]
# print(distance_list[0])
print("test")
print(distance_list[0][0][60][54])
# print(distance_list[99][5])
