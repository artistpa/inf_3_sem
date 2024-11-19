a = [int(s) for s in input().split()]
t = []
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            t.append(a[i])
            a[i], a[j] = - i ** 10, - j ** 12
for i in range(len(a)):
    for j in range(len(t)):
        if a[i] == t[j]:
            a[i] = - i ** 15
print(max(a))
