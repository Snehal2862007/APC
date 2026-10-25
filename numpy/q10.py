import numpy as np

a = np.arange(1, 17).reshape(4, 4)

print("matrix:\n", a)
print("row sum:", np.sum(a, axis=1))
print("column sum:", np.sum(a, axis=0))