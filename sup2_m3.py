# Superposition of Line Vortex and Line Sink
# Author: Divyaprakash

import sympy
from sympy.abc import x, y
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def vortex_sink(q = -1, L = 1.5):
        r = sympy.sqrt(x**2 + y**2)
        theta = sympy.atan2(y, x)
        return (q * theta - L * sympy.log(r)) / (2 * sympy.pi)

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

xlim = ylim = (-3, 3)
fig, ax = plt.subplots(figsize=(4, 4))
plot_streamlines(ax, u, v, xlim, ylim)


format_axes(ax)

plt.show()




