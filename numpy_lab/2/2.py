import numpy as np
import matplotlib.pyplot as plt

with open("signal03.dat") as file:
    signal = [float(line.rstrip()) for line in file]
print(signal)
signal = np.array(signal)

new_signal = []
for i in range(10):
    new_signal.append(sum(signal[:i+1]) / (i + 1))
for i in range(10, len(signal)):
    new_signal.append(sum(signal[i-9:i+1]) / 10)

fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(signal)
ax[0].grid()
ax[0].set_title("До обработки")
ax[1].plot(new_signal)
ax[1].grid()
ax[1].set_title("После обработки")
plt.savefig("3.jpg")