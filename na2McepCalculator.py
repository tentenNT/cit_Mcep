import numpy as np
import na2McepFunctions as mfunc
import na2McepClass as mclass
import pdb

def distance_checker(template_data, test_data): # フレーム同士での計算
    print(template_data.word, test_data.word)
#     pdb.set_trace()
    distance_array_frames = np.zeros((len(template_data.framedata), len(test_data.framedata))) # タプルで渡す
# 5フレーム用
#     distance_array = np.zeros((5, 5)) # タプルで渡す
    for i in range(len(template_data.framedata)):
# こっちだと5フレーム分だけ計算する
#     for i in range(5):
        for j in range((len(test_data.framedata))):
# 上に同じ
#         for j in range(5):
#             print(i, j, np.linalg.norm(template_data.framedata[i] - test_data.framedata[j]))
            distance_array_frames[i][j] = np.linalg.norm(template_data.framedata[i] - test_data.framedata[j])
#             print(distance_array)
#             pdb.set_trace()

# リスト内包表記にしてみる
#     distance_array = [print(i, j, np.linalg.norm(template_data.framedata[i] - test_data.framedata[j])) for i in range(len(template_data.framedata)) for j in range(len(test_data.framedata))]
#     distance_array[:] = [np.linalg.norm(template_data.framedata[i] - test_data.framedata[j]) for i in range(len(template_data.framedata)) for j in range(len(test_data.framedata))]
# できねえ

#     print(distance_array)
    return distance_array_frames

template_data_list = mclass.readfiles(mclass.template_data_location)
test_data_list = mclass.readfiles(mclass.test_data_location)
# print(template_data_list[2].framedata[0][4])
# こうすればcity011_003.textの0フレーム目の3次元目が取れる

# 単語同士でのマッチング
# distance_array = np.zeros((100, 100))
# distance_array_words = np.zeros((3, 3))
distance_list = [[] for i in range(3)]
# pdb.set_trace()
distance_list_inside = []
# フルサイズ(100*100)
# for template_data in template_data_list:
#     for test_data in test_data_list:
#         distance_checker(template_data, test_data)

# 3*3サイズ
for i, template_data in enumerate(template_data_list[:3]):
    for j, test_data in enumerate(test_data_list[:3]):
        distance_list[i].append(distance_checker(template_data, test_data))


# distance_array[:] = np.array(distance_list)

# リスト内包表記にしてみる(100*100)
# 次元を間違っている
# print(distance_array)
# distance_list = [distance_checker(template_data, test_data) for template_data in template_data_list for test_data in template_data_list]
# リスト内包表記にしてみる(5*5)
# distance_list = [distance_checker(template_data, test_data) for template_data in template_data_list[:5] for test_data in test_data_list[:5]]
# print(distance_list[0])
print("test")
print(distance_list)
distance_array = np.array(distance_list)
# pdb.set_trace()
np.save("distance_array.npy", distance_array)
# print(distance_list[99][5])
