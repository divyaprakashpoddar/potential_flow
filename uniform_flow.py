from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

delta = 0.1
x = np.arange(-1, 1, delta)
y = np.arange(-1, 1, delta)
X, Y = np.meshgrid(x,y)

V = 1
phi = V * X
psi = V * Y

# Surface Plot
#fig1 = plt.figure()
#ax1 = fig1.gca(projection = '3d')
#S = ax1.contour(X, Y, phi)
#S = ax1.scatter3D(X, Y, phi)

# Contour Plot
matplotlib.rcParams['contour.negative_linestyle']= 'solid'
fig2 = plt.figure()
ax2 = fig2.gca()
CS = ax2.contour(X, Y, phi, colors = 'blue')
ax2.clabel(CS, inline=1, fmt = '$\phi$', fontsize=10)
CS = ax2.contour(X, Y, psi, colors = 'red')
ax2.clabel(CS, inline=1, fmt = '$\psi$', fontsize=10)

plt.show()


