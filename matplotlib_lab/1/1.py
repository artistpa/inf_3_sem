import matplotlib.pyplot as plt

with open(input()) as file:
    lines = [line.rstrip() for line in file]
n = int(lines[0])
points = []
x = []
y = []
for i in range(1, n + 1):
    points.append(lines[i].split())
print(points)
for i in range(len(points)):
    for j in range(len(points[i])):
        points[i][j] = float(points[i][j])
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

print(points)
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable = 'box')
for i in range(len(points)):
    ax.plot(x[i], y[i], 'ro', markersize = 0.5)
ax.set_title(f'Number of points: {n}')
#plt.savefig('1.jpg')
plt.show()
