s = input()
k = 0
n = 0
i = 0
while i < len(s):
    if int(s[i]) == 1:
        while int(s[i]) == 1 and i < len(s) - 1:
            k += 1
            i += 1
        if i == len(s) - 1 and int(s[i]) == 1:
            k += 1
        if k > n:
            n = k
        k = 0
    i += 1
print(n)