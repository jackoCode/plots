import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['science', 'notebook', 'grid'])

x = np.linspace(0, 15, 30)
y = np.sin(x) + 0.1*np.random.randn(len(x))
x2 = np.linspace(0, 15, 100)
y2 = np.sin(x2)

plt.figure(figsize=(8,3))
plt.plot(x, y, 'o', label='Data', zorder=100)
plt.plot(x2, y2, label='Fit')
plt.xlabel('Time [s]', fontsize=16)
plt.ylabel('Voltage [V]')
plt.title('Voltage in 3rd Electrode')
plt.legend(loc='upper right', fontsize=12, ncol=2)
plt.ylim(top=2)
plt.show()
