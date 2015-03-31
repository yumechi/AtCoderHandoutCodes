N, M = map(int, input().split())
regs = [2, 3, 4]
oto, rou, aka = 0, 0, 0
if N * regs[0] > M or N * regs[2] < M:
    print("-1 -1 -1")
else:
    aka = (M - M % regs[2]) // regs[2]
    temp = M - aka * regs[2]
    while N > sum([oto, rou, aka]):
        if temp == 1:
            aka -= 1
            if aka < 0:
                print("-1 -1 -1")
                exit(0)
            temp += 4
        elif temp == 2:
            oto += 1
            temp -= 2
        elif temp == 3:
            rou += 1
            temp -= 3
        elif temp == 5:
            oto += 1
            rou += 1
            temp -= 5
        elif temp == 0:
            aka -= 1
            oto += 2
    if sum([oto, rou, aka]) == N:
        print(oto, rou, aka)
    else:
        print("-1 -1 -1")
