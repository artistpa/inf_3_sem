N = int(input())
words = []
for i in range(N):
    words.append([e for e in input().split()])
words = [a for b in words for a in b]
print(words)