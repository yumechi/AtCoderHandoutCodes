# 改良に改良を重ねたけど限界
# JavaでのAC：http://arc036.contest.atcoder.jp/submissions/380640
# その他の提出
# https://arc036.contest.atcoder.jp/submissions/380642
# https://arc036.contest.atcoder.jp/submissions/380635
# https://arc036.contest.atcoder.jp/submissions/380629
# https://arc036.contest.atcoder.jp/submissions/380625
# https://arc036.contest.atcoder.jp/submissions/380615
# https://arc036.contest.atcoder.jp/submissions/380593
# https://arc036.contest.atcoder.jp/submissions/380567

import copy

N, K = map(int, input().split())
slist = list(input())
MODNUM = 1000000007

dp = [[0 for _ in range(K + 2)] for _ in range(K + 2)]
ndp = copy.deepcopy(dp)
dp[0][0] = 1

for t in range(0, N):
    casii = ord(slist[t])
    for i in range(0, K + 1):
        for j in range(0, K + 1):
            if dp[i][j] == 0:
                continue

            if casii == 48 or casii == 63:
                nj = j - 1 if j > 0 else 0
                ndp[i + 1][nj] += dp[i][j]
            if casii == 49 or casii == 63:
                ni = i - 1 if i > 0 else 0
                ndp[ni][j + 1] += dp[i][j]

    for i in range(0, K + 1):
        for j in range(0, K + 1):
            dp[i][j] = ndp[i][j]
            ndp[i][j] = 0

res = 0
for i in range(0, K + 1):
    res += sum(dp[i]) - dp[i][K + 1]

print(res % MODNUM)