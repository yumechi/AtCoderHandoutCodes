N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

mincost = (A + 1) * N

for X in range(N + 1):
    Y = ((N - X) * E - H - B * X) // (D + E) + 1
    Y = 0 if Y < 0 else Y
    mincost = min(A * X + C * Y, mincost)
print(mincost)