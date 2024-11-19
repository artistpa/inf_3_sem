k = []
n = []
for i in range(2):
    k.append(list(input().split()))
for pet in k[0]:
    c = 0
    for person in k[1]:
        if (pet[0] == person[0]):
            c += 1
    if c == 0:
        n.append(pet)
print(*n)