import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['default'])

_ = np.linspace(-1, 1, 100)
x, y = np.meshgrid(_,_)
z = x**2 + x*y

plt.contourf(x,y,z, levels=50, cmap='plasma')
plt.colorbar(label='Temperature [$^\circ C$]')
plt.xlabel('Horizontal Position [m]')
plt.ylabel('Vertical Position [m]')
plt.show()