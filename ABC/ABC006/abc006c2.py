# 老人0 or 1パターン
N, M = map(int, input().split())
if N * 2 > M or N * 4 < M:
    print("-1 -1 -1")
else:
    oto, rou, aka = 0, 0, N
    if M % 2 == 1:
        rou += 1
        M -= 3
        aka = N - 1
    while oto * 2 + aka * 4 != M:
        aka -= 1
        oto += 1
        if aka < 0:
            print("-1 -1 -1")
            exit(0)

    if N == sum([oto, rou, aka]):
        print(oto, rou, aka)
    else:
        print("-1 -1 -1")