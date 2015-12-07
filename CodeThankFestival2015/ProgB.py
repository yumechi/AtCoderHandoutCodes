al = [x for x in input().split()]
bl = [x for x in input().split()]
num = input()
res = []
if num in al:
    res.append(bl[0])
    res.append(bl[1])
if num in bl:
    res.append(al[0])
    res.append(al[1])
res.sort()
res = list(set(res))
res = [int(x) for x in res]
res.sort()
print(len(res))
for r in res:
    print(r)
