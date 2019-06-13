import numpy as np
from pathlib import Path

class Mcep_class:
    def __init__(self, word, frame, dimension):
        self.word = word
        self.frame = frame
        self.dimension = dimension

template_data_location = "city011"
test_data_location = "city012"

def readfiles(data_location):
    for i in range(1, 101):
        if i < 10:
            yield Path(data_location+"/" + data_location + "_00{}.txt".format(i))
        elif i < 100:
            yield Path(data_location+"/" + data_location + "_0{}.txt".format(i))
        else:
            yield Path(data_location+"/" + data_location + "_{}.txt".format(i))
 
# 読み込み方
# template_data_list = list(readfiles(template_data_location))
# test_data_list = list(readfiles(test_data_location))


