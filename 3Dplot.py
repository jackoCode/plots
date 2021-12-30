import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

plt.style.use(['default'])

_ = np.linspace(-1, 1, 100)
x, y = np.meshgrid(_,_)
z = x ** 2 + x * y

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x, y, z, cmap='coolwarm', linewidth=0, antialiased=False)
ax.view_init(elev=10, azim=0)


def animate(i):
    ax.view_init(elev=10, azim=3 * i)


ani = animation.FuncAnimation(fig, animate, frames=120, interval=50)
ani.save('ani2.gif', writer='pillow', fps=30, dpi=100)
plt.show()