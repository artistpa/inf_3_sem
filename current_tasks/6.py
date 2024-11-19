n = int(input())
ch = []
chan = []
chans = []
for i in range(n):
    ch.append(input().split('\n'))
for i in range(len(ch)):
    chan.append(ch[i][0].split(':'))
for i in range(len(chan)):
    chans.append(chan[i][0])
    chans.append(chan[i][1].split(','))
bots = [int(e) for e in input().split(',')]
id1 = int(input())
print(chans)