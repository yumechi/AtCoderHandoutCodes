n, k = map(int, input().split())
sli = [int(input()) for _ in range(n)]
if 0 in sli:
    print(n)
    exit(0)
if k == 0:
    print(0)
    exit(0)
sidx = 0
eidx = 0
sumnum = 1
res = 0
for i in range(n):
    sumnum *= sli[i]
    if sumnum > k:
        eidx = i
        res = max(res, eidx - sidx)
        while sumnum > k:
            sumnum /= sli[sidx]
            sidx += 1
print(max(res, n - sidx))
