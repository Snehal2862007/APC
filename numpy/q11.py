import numpy as np

a = np.arange(1, 21)

print("first 5:", a[:5])
print("last 5:", a[-5:])
print("alternate:", a[::2])
print("reverse:", a[::-1])