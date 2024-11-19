import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open("start.txt") as file:
    unn = [float(line.rstrip()) for line in file]
un0 = np.array(unn)
#print(len(unn))

def un1(un):
    A = np.eye(len(un))
    for i in range(len(A)):
        A[i][i - 1] = -1
    return un - 0.5 * np.dot(A, un)

transformed_data = []
transformed_data.append(un0)
for i in range(1, 255):
    transformed_data.append(un1(transformed_data[i-1]))

#print(transformed_data)

t = np.linspace(0, 49, 50)
#print(t)

fig = plt.figure()
axis = plt.axes(xlim=(0, 50), ylim=(0, 10))
line, = axis.plot(t, transformed_data[0], lw=1, color='blue')
plt.grid()

def update_plot(i):
    line.set_data(t, transformed_data[i])
    plt.title("U(t)")
    return line

anim = animation.FuncAnimation(fig, update_plot, frames=255, interval=50)
anim.save('un.gif', writer='pillow')
plt.show()
