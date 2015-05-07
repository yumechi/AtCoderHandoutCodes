N = int(input())
aset = set(map(int, input().split()))
resset = set()
for elem in aset:
    while elem % 2 == 0:
        elem //= 2
    resset.add(elem)
print(len(resset))