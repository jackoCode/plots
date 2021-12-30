import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['science', 'notebook', 'grid'])

res_a1 = 0.2*np.random.randn(1000)+0.4
res_b1 = 0.25*np.random.randn(1000)+0.4
res_a2 = 0.21*np.random.randn(1000)+0.3
res_b2 = 0.22*np.random.randn(1000)+0.3

textstr1 = '\n'.join((
    r'$\sigma_a=%.4f$' % (np.std(res_a1)),
    r'$\sigma_b=%.4f$' % (np.std(res_b1))))

textstr2 = '\n'.join((
    r'$\sigma_a=%.4f$' % (np.std(res_a2)),
    r'$\sigma_b=%.4f$' % (np.std(res_b2))))

fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
ax = axes[0]
ax.hist(res_a1, bins=30, density=True, histtype='step', label='Method a', color='blue')
ax.hist(res_b1, bins=30, density=True, histtype='step', label='Method b', color='red')
ax.text(0.05, 0.81, textstr1, transform=ax.transAxes, bbox=dict(facecolor='white', edgecolor='black'), size=12)
ax.legend(fontsize=10, fancybox=False, edgecolor='black')
ax.set_ylabel('Frequency')
ax.set_title('Trial 1')
ax = axes[1]
ax.hist(res_a2, bins=30, density=True, histtype='step', label='Method 1', color='blue')
ax.hist(res_b2, bins=30, density=True, histtype='step', label='Method 2', color='red')
ax.text(0.05, 0.81, textstr2, transform=ax.transAxes, bbox=dict(facecolor='white', edgecolor='black'), size=12)
ax.set_title('Trial 2')
fig.text(0.5, -0.04, '$\Delta E$ [Joules]', ha='center', size=20)
plt.savefig('trial.png', dpi=200)
plt.show()