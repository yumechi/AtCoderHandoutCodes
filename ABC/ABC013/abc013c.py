N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

mincost = (A + 1) * N

for i in range(N + 1):
    for j in range(0, N + 1 - i):
        costA = A * i
        choiceB = B * i
        costC = C * j
        choiceD = D * j
        if H + choiceB + choiceD - (E * (N - i - j)) > 0:
            mincost = min(mincost, costA + costC)

print(mincost)