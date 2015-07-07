n, m = map(int, input().split())
btab, restab = [], []

for _ in range(n):
    btab.append(list(map(int, list(input()))))
    restab.append([0] * m)

for i in range(n):
    for j in range(m):
        if btab[i][j] > 0:
            b = btab[i][j]
            restab[i+1][j] += b
            btab[i][j] -= b
            btab[i+1][j-1] -= b
            btab[i+1][j+1] -= b
            btab[i+2][j] -= b

for res in restab:
    print("".join(map(str, res)))
