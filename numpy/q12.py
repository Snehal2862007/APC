import numpy as np

a = np.array([10, 60, 20, 80, 30, 90, 40, 70, 50, 100])

a[a > 50] = 0

print(a)