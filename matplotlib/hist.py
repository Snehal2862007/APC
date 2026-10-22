
import matplotlib.pyplot as plt

# Student marks
marks = [45, 56, 67, 78, 89, 90, 67, 56, 45, 78,
         88, 92, 76, 65, 54, 73, 81, 69, 95, 60]

# Create histogram
plt.hist(marks, bins=5, edgecolor='black')

# Add title and labels
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

# Display histogram
plt.show()
