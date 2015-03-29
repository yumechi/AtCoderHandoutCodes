# 速度が足らない？ Javaで通した http://indeednow-finala-open.contest.atcoder.jp/submissions/370999
N, M = map(int, input().split())
dp = [[[0 for _ in range(0, 101)] for _ in range(0, 101)] for _ in range(0, 101)]
for _ in range(0, N):
    a, b, c, w = map(int, input().split())
    if dp[a][b][c] < w:
        dp[a][b][c] = w

for i in range(0, 101):
    for j in range(0, 101):
        for k in range(0, 101):
                t = dp[i][j][k]
                if i > 0 and t < dp[i-1][j][k]:
                    t = dp[i-1][j][k]
                if j > 0 and t < dp[i][j-1][k]:
                    t = dp[i][j-1][k]
                if k > 0 and t < dp[i][j][k-1]:
                    t = dp[i][j][k-1]
                dp[i][j][k] = t

for _ in range(0, M):
    a, b, c = map(int, input().split())
    print(dp[a][b][c])