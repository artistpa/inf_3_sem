def f(n):
    a = [0] * 100
    a[0], a[1] = 0, 1
    for i in range(2, 60):
        a[i] = a[i-1] + a[i-2]
    return a[n-1]

x = int(input())
print(f(x))