import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("first:", a[0, 0, 0])
print("last:", a[-1, -1, -1])
print("index [0,1,2]:", a[0, 1, 2])
print("index [1,2,3]:", a[1, 2, 3])