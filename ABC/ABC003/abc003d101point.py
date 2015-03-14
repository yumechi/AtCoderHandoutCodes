import math

def getcomb(x, y, N):
    return listmap[x * y][N] if x > 0 and y > 0 else 0

MODNUM = 10 ** 9 + 7

R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())

N = D + L
tablePattern = (R - X + 1) * (C - Y + 1) % MODNUM

# 毎回コンビネーションの計算をしていたら間に合わないので一回で表を作る
# X < 2 or Y < 2 の対策のため，やや多めに0を埋めておく
# パスカルの三角形
listmap = [[0 for j in range(910)] for i in range(910)]
for i in range(0, 901):
    listmap[i][0] = listmap[i][i] = 1
    for j in range(1, i):
        listmap[i][j] = listmap[i - 1][j] + listmap[i - 1][j - 1] % MODNUM

putPattern = getcomb(X, Y, N)
putPattern -= getcomb(X - 1, Y, N) * 2 + getcomb(X, Y - 1, N) * 2
putPattern += getcomb(X - 1, Y - 1, N) * 4 + getcomb(X - 2, Y, N) + getcomb(X, Y - 2, N)
putPattern -= getcomb(X - 1, Y - 2, N) * 2 + getcomb(X - 2, Y - 1, N) * 2
putPattern += getcomb(X - 2, Y - 2, N)
print(tablePattern * listmap[N][D] * putPattern % MODNUM)