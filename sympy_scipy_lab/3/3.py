import sympy as sm
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sm.Symbol('x')
y = sm.Function('y')
res = sm.dsolve(sm.Derivative(y(x), x) + 2 * y(x), y(x), ics={y(0):sm.sqrt(2)})
print(res)

sm.plot(sm.sqrt(2)*sm.exp(-2*x), xlim=(0,10), ylim=(0,1.5), )

def func1(x, y):
    return -2 * y

T = 10
y0 = [np.sqrt(2)]
solution = sp.integrate.solve_ivp(func1, (0.0, T), y0=y0, t_eval=np.linspace(0.0, T, 101))

x = solution.t
x = np.array(x)
f = np.sqrt(2)*np.exp(-2*x)
plt.plot(solution.t, solution.y[0,:], '-ro')
plt.plot(x, f, '-bo')
plt.grid()
plt.show()

plt.plot(x, f - solution.y[0,:], '-go')
plt.show()