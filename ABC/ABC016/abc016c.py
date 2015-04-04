N, M = map(int, input().split())
flist = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    flist[a].append(b)
    flist[b].append(a)

for i in range(N):
    flist[i].append(i)
    flist[i] = set(flist[i])

for man in flist:
    ng = man
    ftof = set()
    for f in man:
        ftof = ftof | (flist[f] - ng)
    print(len(ftof))