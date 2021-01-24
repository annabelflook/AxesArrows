import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# Normal Distribution for plotting
mu = 0
sigma = 1
x1 = -2
x2 = 2

x = np.arange(x1, x2, 0.001)
x_all = np.arange(-4, 4, 0.001)

y = norm.pdf(x, 0, 1)
y2 = norm.pdf(x_all, 0, 1)

# Set up figure, axes and plot
fig, ax = plt.subplots(figsize=(9,6))
plt.style.use('seaborn-white')

ax.plot(x_all, y2, 'black')
ax.set_title('Axes ending with arrows', size=20)


# Plot arrows that follow the axes line. Note the head_width/head_length are inverted.
# x-axis arrow
ax.arrow(-4, 0, 0, 0.44, head_width = 0.1, head_length = 0.01, fc='black')
#y-axis arrow
ax.arrow(-4, 0, 8.1, 0, head_width = 0.01, head_length = 0.1, fc='black')

# X-axis
# xlim set to account for head_width of 0.1
ax.set_xlim([-4.1, 4.2])
ax.set_xlabel('x-axis', font='Times New Roman', size=16)

# Y-axis
# ylim set to account for head_width of 0.01
ax.set_ylim([-0.01, 0.45])
ax.set_ylabel('y-axis', font='Times New Roman', size=16)

# Set all original spines to not be visible
for spine in ax.spines:
    ax.spines[spine].set_visible(False)

# Lengthen ticks to meet axes
ax.tick_params(direction='in', length=6)
              
plt.show()
