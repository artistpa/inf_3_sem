a = [e for e in input().split()]
sum = 0

for i in range(len(a)):
    try:
        a[i] = int(a[i])
    except:
        continue

for i in range(len(a)):
    if type(a[i]) == int:
        sum += a[i]

print(sum)

