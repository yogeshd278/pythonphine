import numpy as np
import mpl_scatter_density
import matplotlib.pyplot as plt

# Generate fake data

N = 10000000
x = np.random.normal(4, 2, N)
y = np.random.normal(3, 1, N)

# Make the plot - note that for the projection option to work, the
# mpl_scatter_density module has to be imported above.

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
#ax.scatter_density(x, y)
ax.set_xlim(-5, 10)
ax.set_ylim(-5, 10)

#fig.savefig('gaussian.png')
density = ax.scatter_density(x, y)
fig.colorbar(density, label='Number of points per pixel')
fig.savefig('demo_files/gaussian_colorbar.png')

plt.show()