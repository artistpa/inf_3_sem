words = open(input()).read().split()
words.sort(key=len, reverse=True)
print(words[0])

