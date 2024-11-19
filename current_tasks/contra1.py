a = [int(e) for e in input().split()]
N = int(input())
a = sorted(a)
k = len(a) - N
while k < len(a):
    print(a[k])
    k += 1

