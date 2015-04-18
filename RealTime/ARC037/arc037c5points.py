N, K = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
alist.sort()
blist.sort()
table = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        table[i][j] = alist[i] * blist[j]
l = []
for i in range(N):
    l.extend(table[i])
l.sort()
print(l[K - 1])