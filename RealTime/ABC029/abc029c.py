n = int(input())
wl = ["a", "b", "c"]
res = ["a", "b", "c"]
for i in range(n-1):
    for j in range(len(res)):
        for k in range(3):
            res.append(res[j] + wl[k])

res.sort()
for r in res:
    if len(r) == n:
        print(r)
