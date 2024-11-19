import matplotlib.pyplot as plt

with open("frames.txt") as file:
    lines = [line.rstrip() for line in file]
points = []
for i in range(len(lines)):
    points.append(lines[i].split())
for i in range(len(points)):
    for j in range(len(points[i])):
        points[i][j] = float(points[i][j])
x = []
y = []
for i in range(int(len(points) / 2)):
    x.append(points[2 * i])
    y.append(points[2 * i + 1])
k = 0

fig, axs = plt.subplots(nrows = 3, ncols = 2, figsize = (12, 6))
fig.tight_layout()
plt.subplots_adjust(hspace=0.5)
for i in range(3):
    for j in range(2):
        axs[i][j].plot(x[k], y[k])
        axs[i][j].set_title(f"Frame {k}", fontsize = 10)
        axs[i][j].minorticks_on()
        axs[i][j].grid(which = "major", alpha = 0.6)
        axs[i][j].grid(which = "minor", alpha=0.3)
        axs[i][j].set_xlim(0, 16)
        axs[i][j].set_ylim(-9, 12)
        k += 1
#plt.savefig("evolution.jpg")
plt.show()