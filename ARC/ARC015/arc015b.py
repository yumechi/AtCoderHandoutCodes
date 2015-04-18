N = int(input())
table = [0 for _ in range(6)]
for _ in range(N):
    maxT, minT = map(float, input().split())
    if maxT >= 35:
        table[0] += 1
    if 30 <= maxT < 35:
        table[1] += 1
    if 25 <= maxT < 30:
        table[2] += 1
    if minT >= 25:
        table[3] += 1
    if 0 <= maxT and minT < 0:
        table[4] += 1
    if maxT < 0:
        table[5] += 1
print(" ".join(list(map(str, table))))