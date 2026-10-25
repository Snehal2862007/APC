import numpy as np

a = np.arange(1, 28).reshape(3, 3, 3)

b = a.flatten()

print("flattened:", b)
print("sum:", np.sum(b))
print("average:", np.mean(b))
print("maximum:", np.max(b))
print("minimum:", np.min(b))