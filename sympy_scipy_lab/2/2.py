import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

with open("large.txt") as file:
    lines = [line.rstrip() for line in file]

F = []
n = int(lines[0])

for i in range(1, n + 1):
    F.append(lines[i].split())
Au = [[float(eachVal) for eachVal in row] for row in F]

c = lines[n+1].split()
bu = [float(val) for val in c]

A = np.array(Au)
b = np.array(bu)
#print(A)
#print(b)
x = sp.linalg.solve(A, b)
print(x)
print(A @ x - b)
t = np.arange(0, len(x))

plt.bar(t,x)
plt.show()