try:
    with open(input()) as file:
        lines = [line.rstrip() for line in file]
    sam = []
    for i in range(len(lines)):
        sam.append(lines[i].split(';'))
    for i in range(len(sam)):
        for j in range(1, len(sam[i])):
            sam[i][j] = int(sam[i][j])
    sum = [0] * len(sam)
    for i in range(len(sam)):
        for j in range(1, len(sam[i])):
            sum[i] += sam[i][j]
    nmin = sum.index(min(sum))
    nmax = sum.index(max(sum))
    print(sam[nmax][0], sum[nmax])
    print(sam[nmin][0], sum[nmin])
except:
    print("no data")

