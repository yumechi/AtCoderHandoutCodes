N, K = map(int, input().split())
rlist = [int(x) for x in input().split()]

rlist.sort()

rate = 0
length = len(rlist)
for i in range(0, K):
    rate = (rate + rlist[length - K + i]) / 2

print(rate)