N, K = map(int, input().split())
slist = list(input())
MODNUM = 1000000007

dp = [[[0 for _ in range(K + 2)] for _ in range(K + 2)] for _ in range(N + 1)]
dp[0][0][0] = 1

for t in range(0, N):
    casii = ord(slist[t])
    for i in range(0, K + 1):
        for j in range(0, K + 1):
            if dp[t][i][j] == 0:
                continue

            if casii == 48 or casii == 63:
                nj = j - 1 if j > 0 else 0
                dp[t + 1][i + 1][nj] += dp[t][i][j]
            if casii == 49 or casii == 63:
                ni = i - 1 if i > 0 else 0
                dp[t + 1][ni][j + 1] += dp[t][i][j]

res = 0
for i in range(0, K + 1):
    res += sum(dp[N][i]) - dp[N][i][K + 1]

print(res % MODNUM)