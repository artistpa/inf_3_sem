data = []
check = True
n = [int(e) for e in input().split(' ')]
k = int(input())
for i in range(k):
    a = [int(e) for e in input().split(' ')]
    data.append(a)
for i in range(k):
    if (data[i][1] > n[0] or data[i][3] > n[1]):
        check = False
for i in range(k):
    for j in range(k):
        if (i != j and ((data[i][0] > data[j][0] and data[i][0] < data[j][1]) or (data[i][1] > data[j][0] and data[i][1] < data[j][1]) or (data[i][2] > data[j][2] and data[i][2] < data[j][3]) or (data[i][3] > data[j][2] and data[i][3] < data[j][3]))):
            check = False
if (check == True):
    print("correct")
else:
    print("broken")