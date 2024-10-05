import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Function to generate a random vector of 1024 points
def generate_random_vector():
    return np.random.rand(1024)

# Function to update the plot with a new vector
def update_plot(frame):
    vector = generate_random_vector()
    line.set_ydata(vector)
    return line,

# Set up the figure and axis
fig, ax = plt.subplots()
vector = generate_random_vector()
line, = ax.plot(vector)

# Set up the animation
ani = FuncAnimation(fig, update_plot, blit=True)

# Show the plot
plt.show()