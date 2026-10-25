import numpy as np

a = np.random.randint(1, 101, (3, 4, 5))

b = a.flatten()
avg = np.mean(b)

print("original:\n", a)
print("flattened:", b)
print("greater than 50:", b[b > 50])
print("even numbers:", b[b % 2 == 0])
print("less than average:", b[b < avg])