m = [int(e) for e in input().split()]
n = int(input())
k = []
f = [0][0]
for i in range(n):
    k.append(list(input().split()))
for i in range(n):
    for j in range(3):
        k[i][j] = int(k[i][j])
print(k)
for i in range(m[0]):
    for j in range(m[1]):
        for e in range(n):
            if (k[n][3])
'''for i in range (n):
    if (k[i][1] - k[i][3] >= 0 and k[i][2] - k[i][3] >= 0):
        number -= (2 * k[i][3] + 1) ** 2
    if (k[i][1] - k[i][3] >= 0 and k[i][2] - k[i][3] < 0):
        number -= (2 * k[i][3] + 1) ** 2
        number += (2 * k[i][3] + 1) * abs(k[i][2] - k[i][3])
    if (k[i][1] - k[i][3] < 0 and k[i][2] - k[i][3] >= 0):
        number -= (2 * k[i][3] + 1) ** 2
        number += (2 * k[i][3] + 1) * abs(k[i][1] - k[i][3])
    if (k[i][1] - k[i][3] < 0 and k[i][2] - k[i][3] < 0):
        number -= (2 * k[i][3] + 1) ** 2
        number += (2 * k[i][3] + 1) * abs(k[i][1] - k[i][3])
