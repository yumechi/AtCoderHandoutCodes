N = int(input())
nlist = list(map(int, input().split()))
count = 0
for i in nlist:
    mi = i % 6
    if mi > 3:
        count += mi - 3
    if mi == 0:
        count += 3
    if mi == 2:
        count += 1

print(count)