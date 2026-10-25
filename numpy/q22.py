import numpy as np

a = np.random.randint(1, 101, (3, 4, 5))

print("array:\n", a)
print("mean:", np.mean(a))
print("median:", np.median(a))
print("standard deviation:", np.std(a))
print("variance:", np.var(a))
print("minimum:", np.min(a))
print("maximum:", np.max(a))