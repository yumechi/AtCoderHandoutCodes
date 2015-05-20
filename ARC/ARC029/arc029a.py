n = int(input())
li = [int(input()) for _ in range(n)]
res = 99999
for i in range(n ** 2):
    t = i
    plateA = 0
    plateB = 0
    for j in range(n):
        if t & 1 == 1:
            plateA += li[j]
        else:
            plateB += li[j]
        t >>= 1
    res = min(res, max(plateA, plateB))
print(int(res))
