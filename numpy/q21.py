
import numpy as np

a = np.random.randint(1, 101, (2, 3, 4))

print("original:\n", a)

a[a > 50] = 0

print("updated:\n", a)