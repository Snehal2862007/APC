import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("array:\n", a)
print("dimensions:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)