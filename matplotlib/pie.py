import matplotlib.pyplot as plt
labels = ['Java', 'Python', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
plt.pie(
    sizes,
    labels=labels
)
plt.title("Programming Language Preferences")
plt.show()
