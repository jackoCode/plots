import numpy as np
import matplotlib.pyplot as plt

w = 3
_ = np.linspace(-3,3,100)
X, Y = np.meshgrid(_,_)
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)

fig, axes = plt.subplots(2,2,figsize=(5,5))
ax = axes[0][0]
ax.streamplot(X, Y, U, V)
ax = axes[0][1]
ax.streamplot(X, Y, U, V, color=speed)
ax = axes[1][0]
lw = 5*speed / speed.max()
ax.streamplot(X, Y, U, V, linewidth=lw)
ax = axes[1][1]
seed_points = np.array([[0,1], [1,0]])
ax.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn', start_points=seed_points)
ax.grid()
plt.show()