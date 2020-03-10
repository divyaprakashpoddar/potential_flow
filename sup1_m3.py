# Superposition of Uniform Stream and Dobulet

import sympy
from sympy.abc import x, y
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def cylinder_flow():
        r = sympy.sqrt(x**2 + y**2)
        theta = sympy.atan2(y, x)
        return (sympy.sin(theta) * (r - 1/r))

def velocity_field(psi):
        u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
        v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
        return u,v

def plot_streamlines(ax, u, v, xlim=(-1, 1), ylim=(-1, 1)):
    x0, x1 = xlim
    y0, y1 = ylim
    Y, X =  np.ogrid[y0:y1:100j, x0:x1:100j]
    ax.streamplot(X, Y, u(X, Y), v(X, Y), color='cornflowerblue')

def format_axes(ax):
    ax.set_aspect('equal')
    ax.figure.subplots_adjust(bottom=0, top=1, left=0, right=1)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    ax.axis('off')

psi = cylinder_flow()
u, v = velocity_field(psi)

xlim = ylim = (-3, 3)
fig, ax = plt.subplots(figsize=(4, 4))
plot_streamlines(ax, u, v, xlim, ylim)

c = plt.Circle((0, 0), radius=1)
#ax.add_patch(c)

format_axes(ax)

plt.show()




