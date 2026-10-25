import numpy as np

a = np.arange(1, 21)

print("even:", a[a % 2 == 0])
print("odd:", a[a % 2 != 0])