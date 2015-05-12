N, T, E = map(int, input().split())
xli = list(map(int, input().split()))
res = -1
 
for x in xli:
    tx = 0
    while tx < (T - E):
        tx += x
 
    if T - E <= tx <= T + E:
        res = xli.index(x) + 1
        break
 
print(res)