import numpy as np

a = np.arange(1, 17).reshape(4, 4)

print("matrix:\n", a)
print("first row:", a[0])
print("last column:", a[:, -1])
print("diagonal:", np.diag(a))
print("second and third rows:\n", a[1:3])