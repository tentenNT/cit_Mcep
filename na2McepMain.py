import numpy as np
import na2McepFunctions as mfunc
import na2McepClass as mclass

a_array = np.zeros(15)
b_array = np.zeros(15)

a_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 11, 12, 13, 14, 15]
print(mfunc.local_distance(a_array, b_array))

