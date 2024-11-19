import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

for n in range(10000, 1000000, 1000):
    x.append(n)
    sum = 0
    for i in range (1, n):
        sum += np.sin(i ** 0.5) / (i ** 0.5)
    y.append(sum)
    print(n)

plt.plot(x, y, 'b')
plt.ylabel("sum")
plt.xlabel("n")
plt.title("Ряд")
plt.minorticks_on()
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.show()