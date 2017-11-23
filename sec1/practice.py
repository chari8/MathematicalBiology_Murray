import numpy as np
from scipy.integrate import odeint
import math
import matplotlib.pyplot as plt
 
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('time')
    plt.ylabel('insect population')
    plt.title('time change of insect population')
    plt.show()
 
def func(u, t, q, r):
    return r*u*(1-u/q)-u**2/(1+u**2)
     
q = 10
r = 0.5
u0 = 10
t = np.arange(0, 100, 0.01)
 
u1 = odeint(func, u0, t, args=(q, r))
 
q = 10
r = 0.2
u0 = 10
t = np.arange(0, 100, 0.01)
 
u2 = odeint(func, u0, t, args=(q, r))
 
q = 10
r = 0.1
u0 = 10
t = np.arange(0, 100, 0.01)
 
u3 = odeint(func, u0, t, args=(q, r))
 
plt.plot(t, u1, '+-.', t, u2,'s-',t,u3,'b-')
plt.show()
