# Author : Hermann Kenko Tanfoudie
# Date : 0/11/2025
# Description : This program is a simple example of how to use numpy and matplotlib libraries in python
# to generate a plot of a function.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the figure size
plt.figure(figsize=(10, 6))

#Histogram plot
data = np.random.randn(1000)  # Generate 1000 random numbers
plt.figure()
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)

#Scatter Plot 
x = np.random.rand(50)
y = np.random.rand(50)
plt.figure()
plt.scatter(x, y, color='red', marker='o', alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

#Line Plot
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = np.sin(x)
plt.figure()
plt.plot(x, y, label="Sine Wave", color='green', linewidth=2)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

#Pie Chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 35, 20, 20]
colors = ['red', 'yellow', 'pink', 'brown']
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Pie Chart")

#Area Plot
x = np.arange(1, 11)
y1 = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
y2 = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
plt.figure()
plt.fill_between(x, y1, color="skyblue", alpha=0.5, label="Series 1")
plt.fill_between(x, y2, color="orange", alpha=0.5, label="Series 2")
plt.title("Area Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

#3D Plot (Surface Plot)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D Surface Plot")

#3D Bar Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(5)
y = np.arange(5)
X, Y = np.meshgrid(x, y)
Z = np.random.randint(1, 10, size=(5,5))  # Random heights

for i in range(len(x)):
    for j in range(len(y)):
        ax.bar3d(x[i], y[j], 0, 0.5, 0.5, Z[i, j], color='cyan')

ax.set_title("3D Bar Plot")

# Show all plots
plt.show()
