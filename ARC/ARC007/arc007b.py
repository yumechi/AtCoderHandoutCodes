N, M = map(int, input().split())
disks = [i for i in range(1, N + 1)]
nowlistening = 0
for _ in range(M):
    j = int(input())
    if j != nowlistening:
        nowlistening, disks[disks.index(j)] = disks[disks.index(j)], nowlistening
for i in disks:
    print(i)
