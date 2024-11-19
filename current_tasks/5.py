import sys
size = [int(e) for e in input().split()]
ms = []
for _ in range(size[1]):
    line = list(map(int, sys.stdin.readline().strip().split()))
    ms.append(line)
numberd = int(sys.stdin.readline().strip())
sum = 0
for _ in range(numberd):
    X, Y, D = map(int, sys.stdin.readline().strip().split())
    for deltay in range(Y - D, Y + D + 1):
        for deltax in range(X - D, X + D + 1):
            if 0 <= deltax < size[0] and 0 <= deltay < size[1]:
                sum += ms[deltay][deltax]
                ms[deltay][deltax] = 0
print(sum)