try:
    words = open(input()).read().split()
    key = input()
    key = key.lower()
    d = dict()
    for word in words:
        word = word.lower()
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    print(d[key])
except:
    print(0)

