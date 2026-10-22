import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [80, 90, 75]

plt.plot(subjects, marks)
plt.title("Marks in Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()