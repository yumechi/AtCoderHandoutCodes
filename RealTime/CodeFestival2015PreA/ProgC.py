n, t = map(int, input().split())
al = []
bl = []
diffl = []
asum, bsum = 0, 0
for i in range(n):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)
    diffl.append([a-b, i])
    asum += a
    bsum += b

if asum <= t:
    print(0)
    exit(0)
if bsum > t:
    print(-1)
    exit(0)

res = 0
diffl.sort()
length = n - 1
while asum > t:
    idx = diffl[length][1]
    al[idx] = bl[idx]
    asum -= diffl[length][0]
    res += 1
    length -= 1
print(res)
