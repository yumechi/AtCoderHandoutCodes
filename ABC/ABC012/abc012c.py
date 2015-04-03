n = int(input())
total = 2025
nlist = []
for i in range(1, 10):
    for j in range(1, 10):
        if total - n == i * j:
            nlist.append([i, j])

for i, j in nlist:
    print(i, "x", j)