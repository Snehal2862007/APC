import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("original:\n", a)
print("flattened:", a.flatten())