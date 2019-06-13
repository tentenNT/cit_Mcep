import numpy as np
def array_info(x):
    print("配列のshape", x.shape)
    print("配列の要素のデータ型", x.dtype)
    print("配列の中身\n",x)

def local_distance(a_array, b_array):
        # a_array = numpy.zeros(15)
        # b_array = numpy.zeros(15)
    ans = 0
    for a, b in zip(a_array, b_array):
        ans += (a - b)**2
    ans = np.sqrt(ans)
    return ans
