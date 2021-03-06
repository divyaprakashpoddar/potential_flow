# Superposition of Doublet
# Author: Divyaprakash

import sympy
from sympy.abc import x, y
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def vortex_sink(q = 1, a = 2, L = 1):
        theta1 = sympy.atan2(y, (x + a))
        theta2 = sympy.atan2(y, (x - a))
        return q * (theta1 - theta2) / (2 * sympy.pi)

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

psi = vortex_sink()
u, v = velocity_field(psi)

xlim = ylim = (-4, 4)
fig, ax = plt.subplots(figsize=(5, 5))
plot_streamlines(ax, u, v, xlim, ylim)


format_axes(ax)

plt.show()




