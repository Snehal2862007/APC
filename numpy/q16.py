import numpy as np

marks = np.array([80, 75, 90, 60, 85, 70, 95, 65, 88, 92])

print("highest:", np.max(marks))
print("lowest:", np.min(marks))
print("average:", np.mean(marks))
print("median:", np.median(marks))
print("standard deviation:", np.std(marks))