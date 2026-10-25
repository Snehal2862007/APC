import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("total sum:", np.sum(a))
print("layer sum:", np.sum(a, axis=(1, 2)))
print("row sum:\n", np.sum(a, axis=2))
print("column sum:\n", np.sum(a, axis=1))