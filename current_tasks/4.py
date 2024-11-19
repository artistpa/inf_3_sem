n = int(input())
col = []
sam = []
col1 = []
s = set()
for i in range(n):
    col.append(input().split('\n'))
for i in range(len(col)):
    sam.append(col[i][0].split(';'))
for i in range(n):
    col1.append(sam[i][1].split(','))
for i in range(n):
    for j in range(len(col1[i])):
        col1[i][j] = col1[i][j].replace(" ", "")
        col1[i][j] = col1[i][j].lower()
for i in range(n):
    for j in range(len(col1[i])):
        s.add(col1[i][j])
colours = []
for e in s:
    colours.append(e)
colours.sort()
print(', '.join(colours))


