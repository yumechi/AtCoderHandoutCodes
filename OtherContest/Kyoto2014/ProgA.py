import itertools

tlist = list(map(int, input().split()))
alist = tlist[0:3]
blist = tlist[3:6]
mind = 9999999999999999
for a in list(itertools.permutations(alist)):
    for b in list(itertools.permutations(blist)):
        d = 0
        d += abs(a[0] - b[0])
        d += abs(a[1] - b[1])
        d += abs(a[2] - b[2])
        mind = min(mind, d)
print(mind)