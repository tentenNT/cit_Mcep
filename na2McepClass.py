import numpy as np
from pathlib import Path
import pdb

# 単語数，データロケーションの指定
WORD_SIZE = 100
template_data_location = "city022"
test_data_location = "city021"


class Mcep_class:
    def __init__(self, filename, word, frame, framedata):
        self.filename = filename
        self.word = word
        self.frame = frame
        self.framedata = framedata


# データを使いやすい形に直す関数
def filetouch(path):
    print(path)
    with open(path, "r") as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        framedatas = lines_strip[3:] # この時点では\nで区切られた1次元リスト
        framedata_list = []
        for x in framedatas:
            print(x)
            framedata_list.append([float(x) for x in x.split()]) # float型に一括変換
    return Mcep_class(lines_strip[0], lines_strip[1], lines_strip[2], np.array(framedata_list))


# データ読み込み用の関数
def readfiles(data_location):
    data_lists = []
    for i in range(1, 101):
        if i < 10:
            path = "./" + data_location+"/" + data_location + "_00{}.txt".format(i)
            data_lists.append(filetouch(path))
        elif i < 100:
            path = str("./" + data_location+"/" + data_location + "_0{}.txt".format(i))
            data_lists.append(filetouch(path))
        else:
            path = str("./" + data_location+"/" + data_location + "_{}.txt".format(i))
            data_lists.append(filetouch(path))
    return data_lists
