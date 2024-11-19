'''a = [s for s in input().split()]
words = []
for m in a:
    try:
        words.append(open(m).read().split())
    except:
        continue
s = set()
for i in range(len(words)):
    for j in range(len(words[i])):
        s.add(words[i][j])
l = list(s)
l.sort()
print(*l)'''

s = set()
for path in input().split():
    try:
        with open(path) as f:
            s.update(f.read().split())
    except:
        pass
print(*sorted(s))