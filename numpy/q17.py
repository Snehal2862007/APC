import numpy as np

marks = np.array([45, 67, 89, 56, 78, 90, 34, 65, 87, 76,
                  55, 69, 91, 82, 73, 48, 60, 95, 84, 71])

avg = np.mean(marks)

print("class average:", avg)
print("above average:", marks[marks > avg])