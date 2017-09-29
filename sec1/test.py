import numpy as np
from scipy.integrate import odeint
import math
import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x,y, marker='o')
# plt.plot(x,y)
    plt.xlabel('time')
    plt.ylabel('population')
    plt.title('title')
    plt.show()


def func(u, t, q, r):
    return r*u*(1-u/q)-u**2/(1+u**2)

q = 10
r = 0.5
u0 = 10
t = np.arange(0, 100, 0.01)

u = odeint(func, u0, t, args=(q, r))

draw_graph(t, u)
